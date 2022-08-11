import smtplib
import email.message


def enviar_email(faturamento, quantidade, ticket_medio):
    corpo_email = f"""
    <p>Boa noite!</p>
    <p>Segue em anexo o relatório das vendas por cada loja.</p>
    <p>Faturamento por loja:</p>
    {faturamento.to_html(formatters={'Valor Final': 'R${:,.2f}'.format})}

    <p>Quantidade vendida por loja:</p>
    {quantidade.to_html()}

    <p>Ticket médio dos produto em cada loja</p>
    {ticket_medio.to_html(formatters={'Ticket Médio': 'R${:,.2f}'.format})}

    <p>Qualquer duvida, estou a disposição!</p>
    <p>Att.</p>
    <p>Danilo</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Relatório de vendas por loja"
    msg['From'] = 'fulanosumido@gmail.com'
    msg['To'] = 'fulanosumido@gmail.com'
    password = 'blprcnkvuayuwtzu'
    # Obs.: A chave foi excluída após o uso
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')

