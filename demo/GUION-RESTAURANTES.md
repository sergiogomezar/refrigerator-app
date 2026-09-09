# Guion de presentación — Demo de restaurantes y hoteles

Para narrar en vivo `demo/restaurantes.html`. Mismo motor y misma coreografía que la demo de
hogar, otro guion: grupos de 3 a 20 sedes, un servicio de almuerzo en la sede Centro.

Duración: **3:12**, 39 beats, seis momentos.
Se abre con doble clic, sin servidor y sin internet.

---

## Antes de entrar a la sala

- Abre `demo/restaurantes.html`, pantalla completa con `F`. Se ve bien de 1280×720 para arriba.
- La vista por defecto es **tablet**, a propósito: es la que hay montada en una cocina. `M` pasa a
  móvil si quieres mostrar el caso del encargado que anda con el teléfono.
- `L` activa el bucle, `espacio` pausa, `1` a `6` saltan de momento, `R` reinicia.
- `demo/restaurantes.html#b25` abre pausado en un beat concreto.

**Regla de oro: no leas los subtítulos en voz alta.** Lo que sigue es lo que conviene decir
*además* de lo que se ve.

---

## Para quién es esta demo

Antes de darle play, si hace falta encuadrar:

> "Los sistemas de merma con cámara — Winnow, Orbisk, Leanpath — se venden por cotización a grupos
> grandes. El restaurante mediano latinoamericano queda fuera, y sí es atendible: con un teléfono,
> etiquetas y un sensor de veinte dólares. Ese es el hueco."

Modelo de ingreso: **suscripción por sede, sin comisión de proveedor.** Se dice en pantalla en M5,
y conviene no adelantarlo: en B2B la comisión huele a conflicto de interés.

---

## Si la presentas por videollamada

Lo que cambia respecto de una sala no es el guion, es el canal. Tres cosas se rompen: la
resolución, la latencia y la posibilidad de leer caras.

### Antes de la llamada

- **Presenta en vista de tablet, no en móvil.** Ya es la vista por defecto de esta demo, así que no toques nada. Si por costumbre
  pulsaste `M`, vuelve con `T`: en móvil el texto de la tablet de cocina queda ilegible del otro
  lado de la llamada.
- **Comparte la ventana del navegador, no la pantalla completa.** Compartir todo el escritorio
  obliga a la plataforma a reducir un lienzo más grande y el texto sale peor.
- **Maximiza la ventana y entra en pantalla completa con `F`** antes de compartir. Menos cromo del
  navegador, más pixeles para la demo.
- **Activa la opción de "optimizar para video" si tu plataforma la tiene** (en Zoom es *Optimize
  for video clip*). La demo es animación casi todo el tiempo, y sin eso el compresor sacrifica
  justo el texto pequeño.
- **No compartas el audio del sistema.** La demo no tiene sonido.
- **Ten el guion en otra pantalla o impreso.** Si lo abres en la misma, se ve.
- **Haz una prueba con alguien antes.** Lo único que hay que confirmar es que el subtítulo de abajo
  se lee del otro lado. Si no se lee, la demo se cuenta sola a medias.

### Durante

- **Déjala correr los 3:12 de una, y recién después vuelve atrás.** En una sala puedes pausar y
  conversar sin romper nada; en una llamada, cada interrupción cuesta el doble. El patrón que
  funciona es: play completo, y luego "déjenme volver a dos momentos" con las teclas `1` a `6`.
- **No narres encima de los beats rápidos.** Tu voz llega con medio segundo de retraso y va a
  chocar con el subtítulo. Habla en los tramos donde la pantalla ya se asentó.
- **Las pausas hay que declararlas.** Nadie va a interrumpirte por video. Di "los dejo ver esto
  diez segundos" y calla de verdad.
- **Quieto el cursor.** El puntero compartido se lleva la atención y le agrega ruido al compresor.
  Si necesitas señalar algo, dilo con palabras.

### Los tres puntos donde vale la pena parar

1. **~1:15, los ocho campos del ERP colapsando en la frase (M2).** Es el momento que vende el
   producto. Pausa con `espacio` y déjalo diez segundos.
2. **~1:35, la propuesta costeada (M3).** El dato de que la sustitución mueve el costo de
   alimentos es lo que separa esto de una app de recetas. Párate ahí si la sala es de finanzas.
3. **3:12, la pantalla del día en barras.** No sigas hablando. Deja el gráfico quieto y pregunta.

### Después

La demo es **un solo archivo HTML, sin dependencias y sin internet**. Se puede enviar por correo y
se abre con doble clic. Es el mejor material de seguimiento que hay, y conviene mandarlo *después*
de la llamada, no antes: si lo tienen abierto mientras hablas, van a ir por delante.

Si la conexión falla en vivo, no hay video de respaldo grabado. La salida es reagendar y mandar el
archivo; no intentes narrarlo sin pantalla.

---

## El recorrido

### Apertura · 0:00 – 0:03

Son las 6:40 de la mañana. La cocina abre y nadie ha tocado la tablet.

> "Esto no es un prototipo conectado. Es la visión del producto contada de punta a punta: un
> servicio de almuerzo en una sede, de la apertura a la recepción del día siguiente."

---

### M1 · El turno ya sabe · 0:03 – 0:42

**En pantalla:** el rail muestra lo que el producto ya sabe antes de que nadie toque nada. La app
abre directo en lo que hay que sacar hoy. FEFO ordena 312 lotes y saca tres, con el dinero a la
vista, y cada uno trae debajo **la instrucción**: sácalo completo hoy, al menú del día, envase
abierto. A la derecha, en qué plato de la carta ya fijada ponerlos, con uno marcado para producir
primero. Cierra con el inventario vivo — 3 vencen hoy, 7 bajo el par, 1,8 días de cobertura —, abre el
detalle de cada cámara (qué lote hay y cuánto queda: 6,4 kg de merluza, 18 kg de pollo, 45 kg de
arroz) y termina en el plan del turno: $152.80 en riesgo si esos lotes no salen.

> "El sistema no propone recetas nuevas. La carta ya la fijó el chef. Lo único que hace es decir
> qué plato consume qué lote, y en qué orden."

> "El orden lo decide FEFO sobre caducidad real, no la IA. En una cocina eso no es un detalle:
> es la diferencia entre una inspección limpia y una multa."

**Si tienes que resumir M1 en una frase:** el turno arrancó con la instrucción puesta, sin conteo
de apertura.

---

### M2 · Una frase · 0:42 – 1:26

**En pantalla:** la chef dice *"¿Qué saco para el almuerzo? Vienen 80 cubiertos y me falta un
cocinero."* La IA saca cuatro variables. El contexto aporta dos cosas que nadie tuvo que decir: el
gluten declarado en la reserva de la 1:30 y la dotación del turno. El sistema multiplica la ficha
técnica por 80 cubiertos y cruza las restricciones: 2 platos de 12 entran, 1 queda bloqueado con
el motivo visible. Al final el panel del rail muestra los ocho campos del ERP que la chef tendría
que llenar hoy, y los colapsa en la frase.

> "Fíjense en la división del trabajo. La IA interpreta lo que se dijo. El sistema multiplica
> fichas técnicas y cruza alérgenos. El gluten de esa reserva no es una inferencia: está
> declarado, y detrás hay responsabilidad legal."

**Este es el momento donde suele caer la ficha.** Los ocho campos colapsando en una frase es lo
único que hay que mostrar si solo te dan treinta segundos. Pausa ahí con `espacio`.

---

### M3 · IA / Sistema · 1:26 – 1:56

**En pantalla:** la chef abre el plato bloqueado — que es justo el que termina de agotar el lote.
El sistema dice qué ingrediente bloquea y a qué reserva afecta. La IA propone cambiar harina de
trigo por almidón de maíz, que hay en despensa sin abrir, **y dice qué le hace al costo**: el
plato sube $0.18 por porción, el costo de alimentos pasa de 31,2% a 31,4%. La chef acepta. Solo
entonces el sistema levanta el bloqueo, recalcula la ficha y firma con nombre y hora.

> "Tres actores. La IA propone y no aplica. La chef acepta o rechaza. El sistema recalcula, y es
> el único que puede levantar un bloqueo."

> "Y noten que la propuesta viene costeada. En una cocina, una sustitución que nadie costea es
> una fuga de margen que aparece a fin de mes sin explicación."

Cierra el momento la **ficha técnica completa**: escandallo por porción con el lote, elaboración
paso a paso con tiempos y los puntos críticos — núcleo a 63 °C, salsa en mesa caliente sobre
65 °C, alérgenos declarados. Desde ahí se cierra la producción.

> "Esta es la ficha que ve la partida. Los mismos gramos que están aquí son los que se descuentan
> por cubierto servido, y los mismos que sostienen el costo del plato."

---

### M4 · Cierra el ciclo · 1:56 – 2:20

**En pantalla:** un toque en "Cerrar producción" descuenta nueve insumos por ficha técnica sobre
los 78 cubiertos que se sirvieron de verdad. La merma queda con motivo, hora y responsable, en
dinero. Cuatro insumos quedan bajo el par. Debajo aparecen **las existencias de la cámara, con la
acción de actualizarlas**. El cierre muestra los $89.60 del lote que vencía hoy y salió completo,
y la merma del turno: $29.30. El rail va revelando las cuatro vías: entra por factura, sale por
ficha técnica, repone por par, corrige la cocina.

> "Este es el momento aburrido y es el más importante. Todo sistema de inventario de cocina muere
> aquí: mantenerlo al día cuesta más trabajo que el problema que resuelve."

Y sobre las existencias:

> "Las cantidades están a la vista y se pueden cambiar en cualquier momento. La que registra la
> cocina es la buena, queda firmada con hora, y el sistema recalcula desde ahí. No le pedimos al
> chef que confirme nuestros cálculos."

*Nota:* en la vista de móvil el aviso de "4 insumos bajo el par" se oculta para que la pantalla no
se recorte. Sigue en el rail y reaparece en la orden de M5.

---

### M5 · Al proveedor · 2:20 – 2:45

**En pantalla:** segunda y última frase del turno, *"Pide lo que falta para mañana."* La orden ya
estaba armada sola desde el par de cada insumo, partida en tres — una por proveedor — cada una con
su calendario de entrega, su unidad de compra, su último precio y su mínimo de pedido. Total
$211.80. Y ahí se declara el modelo: suscripción por sede, sin comisión de proveedor.

> "El proveedor no recibe un chat a medianoche. Recibe una orden con cantidad, unidad y fecha de
> entrega, en la unidad que él factura."

> "Y esto es deliberado: no hay comisión de proveedor. En B2B una comisión contamina las cifras de
> costo y huele a conflicto de interés. Freezai se cobra por sede."

---

### M6 · El costo · 2:45 – 3:12

**En pantalla:** a la mañana siguiente llega la mercancía. La IA lee la factura, detecta la línea
que el proveedor cambió y el alza de $0.40 por litro. Los cinco lotes entran con cámara,
caducidad y temperatura de recepción, firmados por quien recibió. Y cierra con **la pantalla del
día en barras**: recaudado $4,182.50, insumos consumidos $1,225.50 — 29,3% de la venta —
desperdiciado $41.90, que es el 1,0%. Debajo: margen sobre insumos $2,957.00, $186.40 ahorrados
hoy por servir el lote en fresco, y el costo de alimentos contra el 31,4% del mes anterior.

> "Dos puntos de costo de alimentos. En un grupo de cuatro sedes eso no es una mejora cosmética:
> es la diferencia entre el año que cierra bien y el que no."

> "Y no es 'menos merma' en abstracto. Es lo que se ahorró por sacar cada lote antes de que
> venciera: $727.70 en el mes."

Si la sala es de operaciones y no de finanzas, tira además del hilo de la bitácora: temperatura de
recepción firmada, HACCP 31 de 31 días, cada movimiento con responsable y hora.

La demo termina sobre esa pantalla, y el rail cambia al panel **"Lo que sigue"**: orden por
mensaje y exportación al ERP hoy, Rappi y Uber Eats por el lado de la oferta después, y punto de
venta y compras del grupo al final.

---

## Las tres frases que no deberías dejar de decir

1. **"La carta ya la fijó el chef. El producto solo dice qué plato consume qué lote, y en qué
   orden."** (M1)
2. **"La propuesta viene costeada. Una sustitución que nadie costea es una fuga de margen."** (M3)
3. **"No hay comisión de proveedor. Nos cobramos por sede."** (M5)

---

## Preguntas que probablemente van a salir

**¿Y esto se integra con el ERP que ya tenemos?**
Es la pregunta más probable de la sala, y hoy la demo solo la enuncia: hay un botón "Exportar al
ERP" en M5 y no se demuestra. Lo honesto es decirlo así. El primer peldaño real es exportar en el
formato que ya usan, que no depende del permiso de nadie.

**¿Quién carga los 312 lotes la primera vez?**
Hay una carga inicial, y no la escondemos. Lo que cambia es lo de después: a partir de ahí el
inventario entra por factura de recepción y sale por ficha técnica, y las correcciones se hacen
sobre cantidades que ya están en pantalla.

**¿Y cuándo tiene que ingresar datos la cocina?**
Cuando quiera. Las cantidades están a la vista en M4 y se editan ahí mismo. La diferencia es que
lo que registra la cocina se toma como cierto — no le pedimos que confirme nuestros cálculos — y
queda firmado con hora, que es exactamente lo que hoy se hace en planilla.

**¿De dónde salen los pares y la cobertura en días?**
En la demo están declarados. En el producto real salen del consumo medido por ficha técnica, que
es el dato que la propia app produce al cerrar cada servicio.

**¿Esto funciona?**
No todavía. Es una coreografía determinista. Lo que sí está definido es la arquitectura de
responsabilidades entre IA y sistema, y eso sí se puede construir.

**¿La voz es real?**
No, y es intencional. Sin audio ni reconocimiento en vivo, para que la demo no falle en una cocina
con ruido, sin internet o con un equipo prestado.

**¿De dónde salen las cifras?**
Son marcadores plausibles, en dólares. Los porcentajes de costo de alimentos no salen de un
cliente real. Los proveedores son genéricos por la misma razón que la geografía: para no discutir
el mercado antes de discutir el producto.

**¿Y el sensor de temperatura?**
La bitácora se afirma, no se ve ocurrir. Si la conversación es de inspección y HACCP, ese es el
momento que falta y vale la pena decir que está identificado.

**¿Sirve para una sola sede?**
Sirve, pero el caso se paga solo a partir de tres. M6 cierra con el consolidado de cuatro sedes
justamente porque ahí es donde la comparación entre sedes empieza a valer más que el número de
cada una.

---

## Si algo sale mal en la sala

| Problema | Tecla |
|---|---|
| Se congeló o alguien tocó algo | `R` reinicia desde cero |
| Hay que saltar a un momento | `1` a `6` |
| Hay que detenerse a conversar | `espacio` — la escena queda completa |
| La proyección se ve chica | `F` pantalla completa |
| Quieren ver el caso del teléfono | `M` móvil, `T` vuelve a tablet |
| Quedó corriendo sola antes de empezar | `L` activa el bucle |
