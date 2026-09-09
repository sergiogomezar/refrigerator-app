# Guion de presentación — Demo de hogar

Para narrar en vivo `demo/index.html`. La demo funciona sin narrador: los subtítulos ya dicen lo
esencial. Este guion es para cuando conviene una voz humana en la sala.

Duración: **3:12**, 39 beats, seis momentos.
Se abre con doble clic, sin servidor y sin internet.

---

## Antes de entrar a la sala

- Abre `demo/index.html`, pantalla completa con `F`. Se ve bien de 1280×720 para arriba.
- La vista por defecto es **móvil** y es la que mejor cuenta la historia en una sala. `T` pasa a
  tablet si la proyección es grande o si alguien pide ver el detalle; `M` vuelve a móvil.
  **Por videollamada la recomendación se invierte** — ver la sección de abajo.
- `L` activa el bucle: al terminar espera 22 segundos y vuelve a empezar. Útil si la demo queda
  corriendo mientras la gente llega.
- Si te toca volver atrás, las etiquetas M1 a M6 del encabezado son botones y las teclas `1` a `6`
  hacen lo mismo. `espacio` pausa, y al pausar la escena queda completa, nunca a medio revelar.
- `demo/index.html#b25` abre pausado en un beat concreto, por si quieres arrancar en un punto.

**Regla de oro: no leas los subtítulos en voz alta.** Están escritos para leerse. Lo que sigue es
lo que conviene decir *además* de lo que se ve.

---

## Si la presentas por videollamada

Lo que cambia respecto de una sala no es el guion, es el canal. Tres cosas se rompen: la
resolución, la latencia y la posibilidad de leer caras.

### Antes de la llamada

- **Presenta en vista de tablet, no en móvil.** Pulsa `T` apenas la abras. La vista de móvil es la que mejor cuenta la historia en una
  sala, pero comprimida y reducida en la ventana de otro, el texto del teléfono queda demasiado
  chico. En tablet todo crece y se lee. El costo es que M4 y M6 dejan la mitad inferior de la
  pantalla vacía; a cambio, se entiende.
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

1. **~1:15, los siete campos colapsando en la frase (M2).** Es el momento que vende el producto.
   Pausa con `espacio`, déjalo diez segundos en pantalla y pregunta si se entiende qué acaba de
   pasar.
2. **~2:05, las existencias editables (M4).** Es donde va a salir la objeción de "¿y quién
   mantiene esto?". Mejor abrirla tú que esperar a que la abran ellos.
3. **3:12, la pantalla del dinero.** No sigas hablando. Deja el gráfico quieto y pregunta.

### Después

La demo es **un solo archivo HTML, sin dependencias y sin internet**. Se puede enviar por correo y
se abre con doble clic. Es el mejor material de seguimiento que hay, y conviene mandarlo *después*
de la llamada, no antes: si lo tienen abierto mientras hablas, van a ir por delante.

Si la conexión falla en vivo, no hay video de respaldo grabado. La salida es reagendar y mandar el
archivo; no intentes narrarlo sin pantalla.

---

## El recorrido

### Apertura · 0:00 – 0:03

El teléfono está dormido, son las 7:02 p.m. de un martes.

> "Esto no es un prototipo funcional. Es la visión del producto contada de punta a punta: una
> noche en una casa, del hambre a la compra."

---

### M1 · La app ya sabe · 0:03 – 0:42

**En pantalla:** el rail de la derecha muestra las cuatro cosas que el producto ya sabe antes de
que nadie toque nada. La app abre directo en el plan de hoy. Salen tres productos que apuran —
pollo, espinaca, crema — y cada uno trae debajo **qué hacer con él**: cocínala hoy o congélala,
úsala completa en dos días, ya está abierta y hay que usarla antes del jueves. A la derecha, cómo
hacerlo esta noche, con una receta marcada como recomendada. Cierra con el inventario vivo —
34 productos, 3 por vencer, 5 bajo el mínimo, 2 abiertos —, se abre el detalle de cada zona
(qué producto hay y cuánto: 500 g de pollo, 2 L de leche, 600 g de mantequilla, 1 kg de arroz) y
cierra con el plan de la noche.

> "Toda app de despensa arranca pidiéndote que cargues tu inventario. Esta arranca sabiendo. Y
> fíjense en lo que devuelve: no es una lista de lo que tienes, es qué hacer con cada cosa."

> "El orden no lo decide la IA. Lo decide FEFO — primero en vencer, primero en salir — sobre
> fechas reales. La IA no opina sobre fechas."

**Si tienes que resumir M1 en una frase:** la app abrió con el plan puesto, no con un formulario.

---

### M2 · Una frase · 0:42 – 1:26

**En pantalla:** Carolina dice *"¿Qué hago de cena? Algo rápido, están Ana y Sofía."* La IA saca
cuatro variables de esa frase. El contexto aporta dos restricciones que nadie tuvo que decir: Ana
evita lácteos y Sofía es alérgica al maní, las dos declaradas en su perfil. El sistema cruza todo
y quedan 2 recetas de 12, más una bloqueada con el motivo visible. Al final el panel del rail
muestra los siete campos que la persona habría tenido que llenar en cualquier app de hoy, y los
colapsa en la frase.

> "Fíjense en la división del trabajo. La IA interpreta lo que se dijo. El sistema decide qué
> sirve y qué no. La alergia de Sofía no es una inferencia: está declarada y es un filtro duro."

**Este es el momento donde suele caer la ficha.** Si solo pudieras mostrar una cosa de toda la
demo, es el panel de los siete filtros colapsando en una frase. Vale la pena hacer una pausa con
`espacio` justo ahí y dejar que la sala lo mire.

---

### M3 · IA / Sistema · 1:26 – 1:56

**En pantalla:** Carolina abre la receta bloqueada. El sistema no dice "no se puede": dice qué
ingrediente bloquea y a quién afecta. La IA propone cambiar crema de leche por crema de coco, que
ya está en la despensa desde junio sin abrir. Ella acepta. Solo entonces el sistema recalcula y
levanta el bloqueo.

> "Tres actores, tres responsabilidades. La IA propone y no aplica. La persona acepta o rechaza.
> El sistema recalcula y es el único que puede levantar un bloqueo."

> "Esta es la regla que atraviesa todo el producto: fechas, cantidades, alergias y dinero nunca
> son una inferencia. Es lo que permite poner esto frente a una familia con una alergia real."

Cierra el momento la **receta completa**: ingredientes ya ajustados a tres porciones, con la
crema de coco marcada como el cambio, y la preparación paso a paso con su tiempo. Desde ahí se
cocina.

> "Y fíjense en los gramos. Los mismos que están aquí son los que el inventario va a descontar en
> el siguiente momento. La receta no es contenido: es la orden de descuento."

---

### M4 · Cierra el ciclo · 1:56 – 2:20

**En pantalla:** un toque en "Cociné esto" descuenta los cuatro ingredientes en su cantidad
exacta. Lo que se agotó, y el arroz que quedó bajo el mínimo de la casa, caen solos en la lista.
Debajo aparecen **las existencias, con la acción de actualizarlas**. El cierre muestra los $8.40
de pollo que vencía mañana y se cocinó hoy. El rail va revelando las cuatro vías por las que el
inventario se mantiene: entra por comprobante, sale por receta, repone por mínimo, corrige la
persona.

> "Este es el momento aburrido y es el más importante del producto. Todas las apps de despensa
> mueren aquí: mantener el inventario al día cuesta más trabajo que el problema que resuelven."

Y sobre las existencias, que conviene narrar despacio:

> "Las cantidades están siempre ahí y se pueden cambiar. La app no calcula y después pide
> permiso: el inventario es el dato de la persona, y lo que ella registra se toma como cierto. El
> sistema se encarga de mantenerlo entre una actualización y la siguiente."

---

### M5 · Al carrito · 2:20 – 2:45

**En pantalla:** segunda y última frase de la noche, *"Pide lo que falta."* La lista ya estaba
armada sola — lo agotado, lo que bajó del mínimo y la leche, que en esta casa nunca puede faltar —
ordenada por pasillo y con total estimado de $21.20. Sale a un canal de domicilio y la comisión
se le declara al usuario en la misma pantalla.

> "Aquí está el negocio. El canal no recibe a alguien navegando un catálogo: recibe un pedido
> armado, con producto, cantidad y unidad."

> "Y la comisión se declara siempre, en la pantalla donde ocurre. En la versión 1 el hogar no
> paga: paga el afiliado."

---

### M6 · El valor · 2:45 – 3:12

**En pantalla:** cincuenta minutos después llega el pedido. La IA lee el comprobante y detecta que
el repartidor sustituyó una marca de leche; el cambio ya está aplicado. Los cinco productos entran
con su zona y su fecha. Y cierra con **la pantalla del dinero de la noche, en barras**: la cena
costó $11.55 cocinada en casa contra $42.00 pedida a domicilio — $30.45 ahorrados — con el
acumulado del mes debajo: $684.20 aprovechados, $38.90 desperdiciados, $47.60 menos que el mes
pasado.

> "El dinero aparece al final y a propósito. No es la promesa con la que abrimos: es la
> consecuencia de haber cerrado el ciclo."

> "Y no es 'menos desperdicio' en abstracto. Es lo que se ahorró por usar lo que ya estaba
> comprado."

La demo termina sobre esa pantalla, y el rail cambia al panel **"Lo que sigue"**: la escalera de
integraciones, con lo que se puede hacer hoy sin permiso de nadie adelante y Rappi y Uber Eats al
final, que es donde realmente están. No hay cartel de cierre.

---

## Las tres frases que no deberías dejar de decir

1. **"La app no te devuelve una lista de lo que tienes: te dice qué hacer con cada cosa."** (M1)
2. **"La IA interpreta. El sistema decide. Fechas, cantidades, alergias y dinero nunca son una
   inferencia."** (M2 o M3)
3. **"El inventario es el dato de la persona; lo que ella registra se toma como cierto."** (M4)

---

## Preguntas que probablemente van a salir

**¿Esto funciona?**
No todavía. Es una coreografía determinista, no un prototipo conectado. Cada dato en pantalla es
coherente con el anterior porque está guionado. Lo que sí está definido es la arquitectura de
responsabilidades entre IA y sistema, y eso sí se puede construir.

**¿La voz es real?**
No, y es intencional. La onda y el subtítulo están sincronizados con el guion, sin audio ni
reconocimiento en vivo, para que la demo nunca falle en una sala con ruido, sin internet o con un
micrófono prestado.

**¿Y cuándo tiene el usuario que ingresar datos?**
Cuando quiera. Las cantidades están a la vista en M4 y se editan ahí mismo. La diferencia con
cualquier app de despensa es doble: el camino por defecto no exige tocar nada, y lo que la persona
sí registra se toma como cierto sin discutirlo. El sistema no le pide que confirme sus propios
cálculos.

**¿Y si la persona nunca actualiza nada?**
El ciclo no se detiene. El inventario se mantiene con lo que entra por comprobante y lo que sale
por receta. Si las cantidades se desvían, la próxima compra o la próxima actualización manual las
vuelve a poner en su sitio.

**¿De dónde sale el "mínimo" de cada producto?**
En la demo está declarado. En el producto real sale del consumo observado: cuántas veces por mes
se repone y en qué cantidad. Es el dato que hoy la persona lleva en la cabeza; la diferencia es
que aquí se mide y dispara la reposición sola.

**¿De dónde salen los precios?**
Son marcadores, en dólares estadounidenses a escala de precios reales de mercado. Cuando se defina
el país se reemplazan por precios verificados y los canales de compra pasan a tener nombres
reales. Es un bloque de HTML, no un rediseño.

**¿Por qué genérico y no un país concreto?**
Para no discutir el mercado antes de discutir el producto. Es la pregunta abierta más grande que
queda, y cambia canales, productos y cifras.

**¿Dónde está el negocio si el hogar no paga?**
En M5. Comisión del afiliado retail o de domicilio por pedido armado. La demo lo declara en
pantalla porque esa transparencia es parte del producto, no una nota al pie legal.

**¿Y si el repartidor trae otra cosa?**
Pasa en M6 y por eso está ahí. La IA lo detecta desde el comprobante y el inventario entra ya
corregido, sin que nadie revise la bolsa contra la lista.

---

## Si algo sale mal en la sala

| Problema | Tecla |
|---|---|
| Se congeló o alguien tocó algo | `R` reinicia desde cero |
| Hay que saltar a un momento | `1` a `6` |
| Hay que detenerse a conversar | `espacio` — la escena queda completa |
| La proyección se ve chica | `F` pantalla completa, `T` vista de tablet |
| Quedó corriendo sola antes de empezar | `L` activa el bucle |
