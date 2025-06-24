async function carregarContatos() {
    const res = await fetch(/api/contatos);
    const contatos = await res.json();
    const lista = document.getElementById("listar-contatos")

    lista.innerHTML = "";
    contatos.forEach(c => {
        const li = document.createElement("li");
        li.innerHTML = `
        ${c.nome} - ${c.telefone} - ${c.email}
        <button onclick="editarContatos(${c.id}, '${c.nome}', '${c.telefone}', '${c.email}')">Editar</button>
        <button onclick="removerContatos(${c.id})">Excluir</button>
        `;
        lista.appendChild(li)
    });
}

async function removerContato(id){
    await fetch("/api/contatos" + id, {method: "DELETE"});
    carregarContatos(); 
}

