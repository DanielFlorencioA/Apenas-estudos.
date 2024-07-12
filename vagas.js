document.addEventListener("DOMContentLoaded", function() {
    // Função para buscar vagas (essa função simula a busca de dados)
    function fetchVagas() {
        // Aqui você pode adicionar a lógica para buscar as vagas de um servidor ou banco de dados
        // No exemplo abaixo, vamos usar vagas simuladas
        return [
            {
                id: 1,
                nome: "Desenvolvedor Web",
                tipo: "Full-time",
                salario: "R$ 4000,00",
                quantidade_vagas: "2",
                escolaridade: "Superior Completo",
                disponibilidade: "Imediata",
                localidade: "São Paulo",
                carga_horaria: "40h semanais",
                descricao: "Responsável por desenvolver e manter aplicações web."
            },
            {
                id: 2,
                nome: "Analista de Dados",
                tipo: "Part-time",
                salario: "R$ 3000,00",
                quantidade_vagas: "1",
                escolaridade: "Superior Completo",
                disponibilidade: "Imediata",
                localidade: "Rio de Janeiro",
                carga_horaria: "20h semanais",
                descricao: "Responsável por analisar dados e gerar relatórios."
            }
        ];
    }

    // Função para exibir as vagas
    function displayVagas(vagas) {
        const jobListings = document.getElementById("job-listings");
        jobListings.innerHTML = ""; // Limpa a lista de vagas

        vagas.forEach(vaga => {
            const jobCard = document.createElement("div");
            jobCard.className = "job-card";

            jobCard.innerHTML = `
                <h2>${vaga.nome}</h2>
                <p><strong>Tipo:</strong> ${vaga.tipo}</p>
                <p><strong>Salário:</strong> ${vaga.salario}</p>
                <p><strong>Quantidade de Vagas:</strong> ${vaga.quantidade_vagas}</p>
                <p><strong>Escolaridade:</strong> ${vaga.escolaridade}</p>
                <p><strong>Disponibilidade:</strong> ${vaga.disponibilidade}</p>
                <p><strong>Localidade:</strong> ${vaga.localidade}</p>
                <p><strong>Carga Horária:</strong> ${vaga.carga_horaria}</p>
                <p><strong>Descrição:</strong> ${vaga.descricao}</p>
                <button onclick="editVaga(${vaga.id})">Editar</button>
            `;

            jobListings.appendChild(jobCard);
        });
    }

    // Função para editar uma vaga
    function editVaga(id) {
        // Aqui você pode adicionar a lógica para redirecionar para a página de edição com o ID da vaga
        window.location.href = `editar_vaga.html?id=${id}`;
    }

    // Busca e exibe as vagas ao carregar a página
    const vagas = fetchVagas();
    displayVagas(vagas);
});
