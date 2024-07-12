<?php
include('conexao_login.php');

$error_message = '';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (isset($_POST['cpf']) && isset($_POST['senha'])) {
        if (strlen($_POST['cpf']) == 0) {
            $error_message = "Preencha seu CPF";
        } else if (strlen($_POST['senha']) == 0) {
            $error_message = "Preencha sua Senha";
        } else {
            $cpf = $mysqli->real_escape_string($_POST['cpf']);
            $senha = $mysqli->real_escape_string($_POST['senha']);

            $sql_code = "SELECT * FROM usuarios WHERE cpf = '$cpf' AND senha = '$senha'";
            $sql_query = $mysqli->query($sql_code) or die("Falha na execução do código SQL: " . $mysqli->error);

            $quantidade = $sql_query->num_rows;

            if ($quantidade == 1) {
                $usuario = $sql_query->fetch_assoc();

                if (!isset($_SESSION)) {
                    session_start();
                }

                $_SESSION['id'] = $usuario['id'];
                $_SESSION['nome_completo'] = $usuario['nome_completo'];

                header("Location: register.html");
                exit(); // Certifique-se de que a execução do script pare após o redirecionamento
            } else {
                $error_message = "Falha ao logar! CPF ou Senha incorretos";
            }
        }
    }
}
?>

<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- CODIGO DA FONTE -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Ubuntu:ital,wght@0,300;0,400;0,500;0,700;1,300;1,400;1,500;1,700&display=swap" rel="stylesheet">
    <!-- FIM DO CODIGO DA FONTE  -->
    <link rel="stylesheet" type="text/css" href="login.css" media="screen">
    <title>Login-page</title>

    <style>

    .error-message {
        color: red;
        margin-top: 10px;
        font-family: "Ubuntu", sans-serif;
        font-size: 0.9em;
    }
    </style>

</head>
<body>
    <div class="painel" id="painel">
        <div class="forma-painel entrar">
            <form action="" method="POST">
                <h1>Entrar</h1>
                <span>Insira as informações</span>
                <?php
                if (!empty($error_message)) {
                    echo '<div class="error-message">' . $error_message . '</div>';
                }
                ?>
                <input type="text" name="cpf" placeholder="CPF 123.456.789.00" pattern="\d{3}\.\d{3}\.\d{3}-\d{2}" title="Formato: 123.456.789-00"/> 
                <input type="password" name="senha" placeholder="Senha" />
                <a href="#">Esqueceu sua Senha?</a>
                <button type="submit">Entrar</button>
            </form>
        </div>
        <div class="painel-inscrever">
            <div class="inscrever">
                <div class="inscrever-painel inscrever-direita">
                    <h1>Olá, tudo bem?</h1>  
                    <p>
                        Registre-se com seus dados para ter acesso às vagas
                    </p>
                    <a href="register.html">
                        <button class="hidden" id="register"> Criar conta</button>
                    </a>
                </div>
            </div>
        </div>
    </div>  
</body>
</html>
