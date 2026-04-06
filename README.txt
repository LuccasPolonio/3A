Instruções para colocar o repositório local no Github

//Comando que cria uma pasta onde será o repositório
mkdir nome-do-repositorio

//Comando de navegação que acessa a pasta do repositório
cd nome-do-repositorio


//Iniciando o Repositório local
git init

//Commit Inicial para indicar ponto de partida
git commit -m "Commit inicial"

//Depois de alterar, criar ou remover qualquer arquivo. Adicione as mudanças na branch desejada
// o ponto " . " sinaliza que todas as modificações serão adicionadas
git add . 

//Commit  para sempre sinalizar mudanças
git commit -m 'Alterações feitas + nome de quem mudou + data da mudança'

//Lançando as mudanças no repositório remoto (Github)
git push origin main
