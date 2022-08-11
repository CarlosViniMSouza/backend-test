# Projeto Teste Back-End 

Você deve ver esse desafio como uma oportunidade de criar um aplicativo *seguindo as melhores práticas de desenvolvimento modernas* (dada a *Stack* de sua escolha), mas também fique à vontade para usar suas próprias preferências de arquitetura (*padrões de codificação, organização de código, bibliotecas de terceiros, etc.*) . Não há problema em usar código vanilla ou qualquer framework ou biblioteca.

## Escopo

Neste desafio você deve **construir uma API para uma aplicação que armazene e gerencie investimentos**, ela deve ter as *seguintes funcionalidades*:

1. __Criação (Create)__ de um investimento com um proprietário, uma data de criação e um valor.

    1. A data de criação de um investimento pode ser hoje ou uma data no passado.

    2. Um investimento não deve ser ou se tornar negativo.

<br/>

2. __Visualizar (View)__ um investimento com seu valor inicial e saldo esperado.

    1. O saldo esperado deve ser a soma do valor investido e os [ganhos][].

    2. Se um investimento já foi retirado, o saldo deve refletir os ganhos desse investimento.

<br/>

3. __Retirada (Withdrawal)__ de um investimento.

    1. A retirada será sempre a soma do valor inicial e seus ganhos, retirada parcial não é suportada.

    2. As retiradas podem ocorrer no passado ou hoje, mas não podem ocorrer antes da criação do investimento ou do futuro.

    3. [Impostos][impostos] precisam ser aplicados aos saques antes de mostrar o valor final.

<br/>

4. __Lista (List)__ de investimentos de uma pessoa.

    1. Esta lista deve ter paginação.

__NOTA:__ `A implementação de uma interface não será avaliada.`

### Calculo de Ganho

O investimento *pagará 0,52% todo mês no mesmo dia da criação do investimento*.

Dado que o ganho é pago mensalmente, **deve ser tratado como [ganho composto][]**, o que significa que a cada novo período (mês) o valor ganho passará a fazer parte do saldo do investimento para o próximo pagamento.

### Taxação

*Quando o dinheiro é retirado, o imposto é acionado.* Os impostos se *aplicam apenas à parte do lucro/ganho* do dinheiro retirado. Por exemplo, se o investimento inicial foi de 1.000,00, o saldo atual é de 1.200,00, então os impostos serão aplicados aos 200,00.

O percentual de imposto *muda de acordo com a idade do investimento:*

    - Se tiver menos de um ano, o percentual será de 22,5% (imposto = 45,00).

    - Se tiver entre um e dois anos, o percentual será de 18,5% (imposto = 37,00).
    
    - Se tiver mais de dois anos, o percentual será de 15% (imposto = 30,00).

## Requisições

1. Crie o projeto usando qualquer tecnologia de sua preferência. Não há problema em usar código vanilla ou qualquer framework ou biblioteca;

2. Embora você possa usar quantas dependências quiser, você deve gerenciá-las com sabedoria;

3. Não é necessário enviar os e-mails de notificação, no entanto, o código necessário para isso seria bem-vindo;

4. A API deve ser documentada de alguma forma.

## Entregas

O código-fonte e as dependências do projeto devem ser disponibilizados no GitHub. Aqui estão os passos que você deve seguir:

1. Fork este repositório para sua conta do GitHub (crie uma conta se você não tiver uma, você precisará trabalhar conosco).

2. Crie uma ramificação de "developement" e confirme o código nela. Não envie o código para a ramificação principal.

3. Inclua um arquivo README que descreva:
    
    - Instruções de construção especiais, se houver.

    - Lista de bibliotecas de terceiros usadas e breve descrição de por que/como elas foram usadas.
    
    - Um link para a documentação da API.

4. Quando o trabalho estiver concluído, crie um pull request de "development" para "main" e nos envie o link.

5. Evite usar commits enormes escondendo seu progresso. Sinta-se à vontade para trabalhar em um branch e usar o `git rebase` para ajustar seus commits antes de enviar a versão final.

## Padrões de codificação

Ao trabalhar no projeto, seja o mais limpo e consistente possível.

## Prazo do projeto

Idealmente, você terminaria o projeto de teste em 5 dias. Não deve demorar mais do que uma semana inteira.

## Garantia da Qualidade

Use a lista de verificação a seguir para garantir a alta qualidade do projeto.

### General

- Em primeiro lugar, o aplicativo deve ser executado sem erros.

- Todos os requisitos definidos acima são atendidos?

- O estilo de codificação é consistente?

- A API está bem documentada?

- A API possui testes unitários?

## Submissão

1. Um link para o repositório do Github.

2. Descreva brevemente como você decidiu sobre as ferramentas que usou.

## Divirta-se codificando 🤘

- Esta descrição do desafio é intencionalmente vaga em alguns aspectos, mas se você precisar de ajuda, sinta-se à vontade para pedir ajuda.

- Se algum parecer fora do seu nível atual, você pode ignorá-lo, mas lembre-se de nos informar sobre isso no pull request.
