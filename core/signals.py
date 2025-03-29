from django.core.mail import send_mail
from datetime import date
from membros.models import Membro

def enviar_felicitacoes():
    hoje = date.today()
    aniversariantes = Membro.objects.filter(
        data_nascimento__month=hoje.month,
        data_nascimento__day=hoje.day
    )
    for membro in aniversariantes:
        send_mail(
            subject='Feliz Aniversário!',
            message=f'Parabéns {membro.nome}! Que Deus continue te abençoando.',
            from_email='igreja@jardimguanabara.com',
            recipient_list=[membro.email],
            fail_silently=True
        )
