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


**Tome muito cuidado com essas credenciais pois elas poder causar um problema de milhões (literalmente). Se o invasor tiver acesso as suas credenciais ele pode fazer tudo que seu usuario tiver permissão, criar maquinas, provisionar servidores, criar dominios, etc...**


# Configuração do Ambiente:

Para que a key seja utilizada no **AWS CLI** precisamos configura-la:

    aws configure


Após rodar este comando irá pedir para preencher um formulario:

    AWS Access Key ID [None]: <Coloque Sua Access Key ID>
    AWS Secret Access Key [None]: <Coloque Sua Secret Key aqui>
    Default region name [None]: us-east-2
    Default output format [None]:


Agora seu ambiente já esta configurado.

# Subir a Infraestrutura:


- Criar os Pares de chave para poder criar a infraestrutura:
    
    ```

    aws ec2 create-key-pair --key-name <NomeDaSuaChave> --query 'KeyMaterial' --output text > <NomeDaSuaChave>.pem

    ```
    Após rodar este comando dentro das pasta deste projeto ao qual vc clonou:

    ```
    aws cloudformation create-stack --stack-name MinhaStack --template-body file://script.yaml --parameters ParameterKey=KeyName,ParameterValue=<NomeDaSuaChave> --capabilities CAPABILITY_NAMED_IAM

    ```
    * Lembresse de substituir o < NomeDaSuaChave >.

- Agora é só esperar a sua infraestrutura subir.

    - Para descobrir o dns do load-balancer para acessar a aplicação basta rodar este comando.

    ```
    aws cloudformation describe-stacks --stack-name MinhaStack --query "Stacks[0].Outputs"
    ```
    - Ficará retornando nulo enquanto não for criado.

    ```
    [
        {
            "OutputKey": "LoadBalancerDNSName",
            "OutputValue": "MinhaS-MyLoa-gsTk95Zh7YQK-365330849.us-east-2.elb.amazonaws.com",
            "Description": "DNS Name of the Application Load Balancer"
        }
    ]
    ```
    - Retornará algo assim quando estiver pronto.

    *observação caso ao acessar o DNS do load-balancer apresente o erro 502 isso ocorre porque as vezes a aplicação demora um pouco para subir.



# Teste de carga:

Basta rodar os comandos a seguir (dentro da pasta do projeto baixado):
- pré-requisito ter python já instalado.

```
pip install locust
```

```
locust -f locust.py
```
Isso abrirá uma aplicação no http://localhost:8089

Selecione o numero de usuarios desejado e qual o crescimento de acessos destes usuarios, e coloque o DNS pego na etapa anterior e selecione o tempo que o teste de carga irá rodar.
![alt text](/images/locust-0.png)


![alt text](/images/locust-1.png)
![alt text](/images/locust-2.png)
![alt text](/images/locust-3.png)


Podemos ver que algumas falhas ocorreram porem isso é devido ao banco de dados ter um limitador de 100 ReadUnits e 100 WriteUnits isso foi feito pois isso é apenas uma aplicação teste mas na verdade deveria ser feito um calculo de quantos usuarios acessam a aplicação por segundo e quantas requisições eles fazem para poder configurar um limitador que sustenta toda essa carga, se deixarmos on-demand poderiamos sofrer riscos como ataques de negação de serviço oque faria a cobrança de chamadas por banco de dados fosse extratosferica.

# Custos:
