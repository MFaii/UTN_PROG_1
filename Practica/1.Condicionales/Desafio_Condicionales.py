"""
Tarifa base:
✅Todas las facturas incluyen un cargo fijo de $7000 además del costo por consumo.
✅El costo por metro cúbico (m³) de agua es de $200/m³.
Bonificaciones y Recargos según tipo de cliente:
✅Cliente Residencial:
Si el consumo es menor a 30 m³, se aplica una bonificación del 10% sobre el costo del consumo.
Si el consumo supera los 80 m³, se aplica un recargo del 15% sobre el costo del consumo.
✅Cliente Comercial:
Si el consumo es superior a 150 m³, se aplica una bonificación del 8% sobre el costo del consumo.
Si el consumo supera los 300 m³, la bonificación aumenta al 12%.
Si el consumo es menor a 50 m³, se aplica un recargo del 5%.
✅Cliente Industrial:
Si el consumo es superior a 500 m³, se aplica una bonificación del 20% sobre el costo del
consumo.
Si el consumo supera los 1,000 m³, la bonificación aumenta al 30%.
Si el consumo es menor a 200 m³, se aplica un recargo del 10%.
Casos especiales:
✅Si el cliente es Residencial y el total de la factura ❕❕❕sin impuestos ni bonificaciones  es menor a $35000, se aplica un descuento adicional del 5%.
✅En todos los casos, se aplica el IVA del 21% sobre el total.
Requerimientos del programa:
TODO: Solicitar al usuario:
✅Cantidad de metros consumidos
✅Tipo de cliente, que puede ser: Residencial, Comercial o Industrial.
Calcular:
Subtotal de consumo.
Bonificaciones, si corresponde
Recargos, si corresponde
Subtotal, con recargos y bonificaciones.
IVA aplicado (21%), si corresponde.
Total final a pagar.
Mostrar en pantalla el desglose de los cálculos.
"""

# Entrada
metros = float(input("Ingrese la cantidad de m3 consumidos: "))
cliente = input(
    "Ingrese el tipo de cliente (Residencial / Comercial / Industrial): "
).lower()

# Tarifas base
cargo_fijo = 7000
precio_m3 = 200

# Subtotal
subtotal_consumo = metros * precio_m3
subtotal_base = subtotal_consumo + cargo_fijo

# Bonificaciones y Recargos
bonificacion = 0
recargo = 0
descuento_adicional = 0

if cliente == "residencial":
    if metros < 30:
        bonificacion = 0.10 * subtotal_consumo
    elif metros > 80:
        recargo = 0.15 * subtotal_consumo
elif cliente == "comercial":
    if metros > 300:
        bonificacion = 0.12 * subtotal_consumo
    elif metros > 150:
        bonificacion = 0.08 * subtotal_consumo
    elif metros < 50:
        recargo = 0.05 * subtotal_consumo
elif cliente == "industrial":
    if metros > 1000:
        bonificacion = 0.30 * subtotal_consumo
    elif metros > 500:
        bonificacion = 0.20 * subtotal_consumo
    elif metros < 200:
        recargo = 0.10 * subtotal_consumo

# Descuento extra por tipo de cliente
if cliente == "residencial" and subtotal_base < 35000:
    descuento_adicional = 0.05 * subtotal_base

# Subtotal con los recargos y descuentos
subtotal_final = subtotal_base - bonificacion + recargo - descuento_adicional

# IVA y precio final
iva = 0.21 * subtotal_final
precio_final = subtotal_final + iva

print(f"Cargo fijo: ${cargo_fijo}")
print(f"Coste por consumo: ${subtotal_consumo}")
print(f"Subtotal base: ${subtotal_base}")
print(f"Descuento aplicado: ${bonificacion}")
print(f"Recargo aplicado: ${recargo}")
print(f"Descuento extra: ${descuento_adicional}")
print(f"Subtotal con descuentos y recargos: ${subtotal_final}")
print(f"IVA: ${iva}")
print(f"Precio final a pagar: ${precio_final}")
