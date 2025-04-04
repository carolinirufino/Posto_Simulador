print('⛽ Bem-vindo(a) ao Posto da Carolini Power 3000! 💻✨')

litros = float(input('Digite a quantidade de litros: '))

if litros <= 0:
    print("🚫 Quantidade inválida. O valor deve ser maior que zero.")
    exit()

tipo = input('Digite o tipo de combustível (E para etanol e D para diesel): ').upper()

if tipo == 'E':
    preco_litro = 4.1
    if litros <= 15:
        desconto = 0.02
    else:
        desconto = 0.04

elif tipo == 'D':
    preco_litro = 6.4
    if litros <= 15:
        desconto = 0.03
    else:
        desconto = 0.05

else:
    print('🚫 Tipo de combustível inválido. Use E para etanol ou D para diesel.')
    exit()

desconto_valor = preco_litro * litros * desconto
valor_a_pagar = preco_litro * litros - desconto_valor

print(f'\n🧾 Total a pagar: R${valor_a_pagar:.2f}')
print(f'💸 Desconto aplicado: R${desconto_valor:.2f}')
print('✅ Obrigada por abastecer com a gente! Volte sempre 🚗💨')
