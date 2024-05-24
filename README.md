# Projeto de Computação em Nuvem

Neste Projeto será abordado assuntos como Load Balancing(Controle de Carga), Instancias Virtuais EC2 (Amazon Elastic Compute Cloud),
Banco de Dados No-SQL(Dynamo DB). E como integra-los via infraestrutura em codigo(CloudFormation).

A infraestrutura em código, como o CloudFormatio é de extrema importancia hoje em dia visando que precisamos de sistemas em alta disponibilidade e segurança contra possiveis falhas de atualização e possiveis modificações gerais. 

Uma das principais vantagens é podermos disponibilizar milhares de sistemas apenas com o executar de um codigo (ja debugado para evitar falhas), podemos facilmente modifica-lo sem medo pois qualquer problema que ocorrer basta apenas rodar o codigo da infraestrutura anterior que tudo voltará a funcionar como novo. Podendo assim uma só pessoa gestionar um sistema como um todo, podendo assim garantir consistencia de codigo, facil debug, facil recuperação e implementação.


#### Passo a Passo de como implementar a infraestrutura disponibilizada nesse repositorio.

# Instalação do AWS CLI:

Para usuarios Linux é mais facil basta rodar uma linha de comando que a magica irá acontecer:

    curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
    unzip awscliv2.zip
    sudo ./aws/install

Já para usuario Windows é simples porem mais trabalhoso:

    https://awscli.amazonaws.com/AWSCLIV2.msi

Abra este link em seu navegador baixe o executavel e siga o passo a passo nele para instalar.


# Criação das credenciais programaticas:

Para criar as credenciais programáticas na AWS, siga os seguintes passos:

1. Acesse o Console de Gerenciamento da AWS em [https://console.aws.amazon.com](https://console.aws.amazon.com).

2. No canto superior direito, clique no seu nome de usuário e selecione "Security Credentials" (Minhas Credenciais de Segurança).

    ![alt text](/images/image-1.png)

3. Na página "My Security Credentials", clique na seção "Access keys" (Chaves de Acesso).
    ![alt text](/images/image-2.png)
4. Clique em "Create New Access Key" (Criar Nova Chave de Acesso).

    ![alt text](/images/image-3.png)

5. Escolha Command Line Interface (CLI), marque a checkbox e clique em **Next**.

6. Será exibida uma janela com as informações da nova chave de acesso. Clique em "Show Access Key" (Mostrar Chave de Acesso) para visualizar a chave de acesso e o segredo.

7. Anote a chave de acesso e o segredo em um local seguro, pois eles serão necessários para autenticar as chamadas à API da AWS.

8. Após anotar as informações, clique em "Close" (Fechar).

Certifique-se de que as credenciais programáticas estejam configuradas corretamente no ambiente em que você está executando o código.