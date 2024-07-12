<?php
$conexao = mysqli_connect("localhost", "root", "", "projeto_site");

// Checar conexão
if (!$conexao) {
    die("NÃO CONECTADO: " . mysqli_connect_error());
}

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $cpf = $_POST['cpf'];
    $cpf = mysqli_real_escape_string($conexao, $cpf);
    $sql = "SELECT cpf FROM usuarios WHERE cpf='$cpf'";
    $retorno = mysqli_query($conexao, $sql);

    if (mysqli_num_rows($retorno) > 0) {
        $message = "CPF JÁ CADASTRADO!";
    } else {
        // Verifica se o arquivo foi enviado
        if (isset($_FILES["enviarcurriculo"]) && $_FILES["enviarcurriculo"]["error"] == 0) {
            // Define o caminho da pasta de currículos
            $pastaCurriculos = "C:/xampp/htdocs/curriculos/";
            
            // Verifica se a pasta existe, se não, cria a pasta
            if (!file_exists($pastaCurriculos)) {
                mkdir($pastaCurriculos, 0777, true);
            }
            
            // Define o caminho completo do arquivo
            $caminhoArquivo = $pastaCurriculos . basename($_FILES["enviarcurriculo"]["name"]);
            
            // Tenta mover o arquivo enviado para a pasta de currículos
            if (!move_uploaded_file($_FILES["enviarcurriculo"]["tmp_name"], $caminhoArquivo)) {
                $message = "Erro ao enviar o currículo.";
                header("Location: register.html?message=" . urlencode($message));
                exit();
            }
        } else {
            $caminhoArquivo = null;
        }

        // Prepara a instrução SQL para evitar SQL injection
        $stmt = $conexao->prepare("INSERT INTO usuarios (nome_completo, cpf, senha, telefone, data_nascimento, genero, caminho_curriculo, experiencia_antecessora) VALUES (?, ?, ?, ?, ?, ?, ?, ?)");
        $stmt->bind_param("ssssssss", $nome_completo, $cpf, $senha, $telefone, $data_nascimento, $genero, $caminhoArquivo, $experiencia_antecessora);
        
        // Define os valores dos parâmetros
        $nome_completo = $_POST['nomecompleto'];
        $senha = $_POST['senha'];
        $telefone = $_POST['telefone'];
        $data_nascimento = $_POST['datanascimento'];
        $genero = $_POST['genero'];
        $experiencia_antecessora = $_POST['experiencia'];
        
        // Executa a instrução SQL
        if ($stmt->execute()) {
            $message = "CONTA CRIADA COM SUCESSO!";
            if ($caminhoArquivo) {
                $message .= " O currículo enviado com sucesso!";
            }
        } else {
            $message = "Erro ao salvar os dados no banco de dados: " . $stmt->error;
        }
        
        // Fecha a instrução
        $stmt->close();
    }
    
    header("Location: register.html?message=" . urlencode($message));
    exit();
}

// Fecha a conexão com o banco de dados
$conexao->close();
?>
