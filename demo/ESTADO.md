# Freezai — Demo de visión de producto · Estado

Documento de traspaso. Si estás retomando este trabajo en una sesión nueva, lee esto primero.

Última actualización: 9 de septiembre de 2026. Checkpoint 11 completado. La demo está terminada.

---

## Qué es esto

Una demo auto-presentada de la visión de producto de Freezai, para mostrarle a Ángel, CEO de Arkus.
No es un prototipo funcional: es una coreografía determinista que recorre seis momentos (M1 a M6)
en 3:12 y explica de qué se trata el producto sin que nadie tenga que narrarlo.

Sigue el guion "Rapid Product Discovery + Voice-First Product Vision Demo". Los cuatro rounds de
discovery ya se ejecutaron y la recomendación fue **GO TO DESIGN**.

## Decisiones tomadas

| Decisión | Valor | Consecuencia |
|---|---|---|
| Espina dorsal narrativa | **"Qué cocino hoy"** | El ahorro aparece como consecuencia al final (M6), no como promesa desde M1. |
| Geografía | **Genérica** | Sin marcas ni país. Productos neutros. Toda cifra va en dólares estadounidenses (USD), a escala de precios reales de mercado. |
| Buyer de la v1 | **Afiliado retail / domicilio** | El hogar usa gratis. La demo cierra en M5 con la comisión declarada al usuario. |

Preguntas abiertas que siguen sin respuesta: si hay entrevistas reales detrás de `docs/features.html`,
y qué país se elige finalmente (cambia canales, productos y cifras).

## Los seis momentos

1. **M1 · La app ya sabe** — 7:02 p.m., cero input. FEFO ordena, salen tres productos por aprovechar, y cada uno trae debajo la **acción sugerida** (cocínala hoy, congélala, úsala en 2 días); la columna derecha marca una receta como recomendada. Cierra con el inventario vivo — por vencer, bajo mínimo, abiertos —, con **el detalle de cada zona** (qué producto hay y cuánto: 500 g de pollo, 2 L de leche, 600 g de mantequilla) y con **el plan de la noche**.
2. **M2 · Una frase** — *"¿Qué hago de cena? Algo rápido, están Ana y Sofía."* La IA extrae cuatro variables, el contexto aporta dos restricciones ya declaradas, el sistema une y filtra: 2 recetas de 12, más una bloqueada con el motivo visible. Cierra con el panel de los 7 filtros colapsando en la frase.
3. **M3 · IA / Sistema** — Carolina abre la receta bloqueada. La IA propone crema de coco (que ya está en la despensa). Ella acepta. **Solo entonces** el sistema recalcula y levanta el bloqueo. Cierra con la **receta completa**: ingredientes ajustados a las porciones y preparación paso a paso, con los gramos que M4 va a descontar.
4. **M4 · Cierra el ciclo** — `Cociné esto` descuenta el inventario solo. Lo agotado y lo que quedó bajo el mínimo caen en la lista, y las **existencias quedan a la vista y editables**: la cantidad que registra la persona es la buena. El rail muestra las cuatro vías por las que el inventario se mantiene: entra por comprobante, sale por receta, repone por mínimo, corrige la persona. Es la respuesta al problema que mata a toda app de despensa: mantener el inventario cuesta más que el problema que resuelve.
5. **M5 · Al carrito** — *"Pide lo que falta."* Lista por pasillo, total estimado, salida al canal, comisión declarada. Es el momento de negocio.
6. **M6 · El valor** — El pedido vuelve solo por comprobante, con la sustitución del repartidor ya aplicada. Recién ahí aparece el dinero, y cierra con la **pantalla del día en barras**: `$11.55` de cena cocinada contra `$42.00` de pedirla, `$30.45` ahorrados esta noche.

## Archivos

```
demo/
  index.html              La demo de hogar. Un solo archivo, sin dependencias, funciona offline.
  restaurantes.html       La demo B2B: grupos de restaurantes y hoteles. Mismo motor, otro guion.
  ESTADO.md               Este documento.
  GUION-HOGAR.md          Guion para narrar la demo de hogar en vivo, con tiempos y preguntas probables.
  GUION-RESTAURANTES.md   Lo mismo para la demo B2B.
  vercel.json             Configuración del despliegue estático en Vercel.
  .vercelignore           Lo que NO se publica: este documento, los guiones, checkpoints y tools.
  checkpoints/            Copias de cada checkpoint anterior. Archivar antes de sobrescribir.
  tools/probe.py          Arnés de medición headless. Ver abajo.
  tools/probe.html        Arnés viejo por iframe. No sirve bajo file://, ver abajo.
docs/                     Dossier, análisis de viabilidad y features. Insumo del discovery.
```

## Cómo correrla

```bash
xdg-open demo/index.html          # hogar
xdg-open demo/restaurantes.html   # restaurantes y hoteles
```

Dura 3:12. Controles: `espacio` reproducir/pausa · `←` `→` beat anterior/siguiente · `1`–`6` saltar a un momento ·
`R` reiniciar · `L` bucle desatendido · `F` pantalla completa · `M`/`T` móvil/tablet.
`demo/index.html#b20` abre pausado en el beat 20.

Para presentarlas en vivo, los guiones con tiempos están en `GUION-HOGAR.md` y
`GUION-RESTAURANTES.md`. El de hogar reemplaza al viejo `GUION.md`, que se eliminó.

## Cómo publicarla

Las dos demos son archivos estáticos hermanos y se publican como un solo sitio de Vercel, con
esta carpeta (`demo/`) como raíz del proyecto. No hay build ni dependencias.

```bash
cd demo
npx vercel login          # una sola vez, abre el navegador
npx vercel link --yes --project freezai-demo
npx vercel deploy --prod --yes
```

Queda `/` con la demo de hogar y `/restaurantes` con la B2B. El selector de la esquina superior
derecha alterna entre las dos: son dos enlaces, no una aplicación, así que funciona igual servido
y abierto con `file://`.

`vercel.json` activa `cleanUrls` y manda no cachear, para que un redespliegue se vea de inmediato
en la sala. `.vercelignore` deja fuera este documento, los guiones, `checkpoints/` y `tools/`:
solo se suben los dos HTML.

## Cómo está construida

Un motor de coreografía con una lista de `beats`. Cada beat es `{ id, dur, moment, say, enter() }`.
`enter()` solo fija estado (agrega clases, revela elementos, muta el DOM); nunca depende de dónde
venía la escena. Por eso `goto(i)` puede reconstruir cualquier punto corriendo los `enter()`
anteriores en orden y saltar sin desincronizarse.

Piezas que conviene entender antes de tocar nada:

- **`later()` / `killPending()` / `flushPending()`** — las revelaciones diferidas se cancelan al cambiar de beat y se *adelantan* al pausar, para que una pausa nunca deje un frame a medio revelar.
- **Vistas** — `.view[data-view="m1".."m6"]`, una activa a la vez. `resetScene()` restaura por `innerHTML` las vistas M3 y M5, que se mutan durante la demo.
- **Atributos de revelación** — `data-r` (M1), `data-q` (M2), `data-s` (M3), `data-t` (M4), `data-u` (M5), `data-v` (M6), `data-l` (traza), `data-i` (chips de intención), `data-f` (los 7 filtros), `data-b`, `data-c`, `data-d` y `data-e` (paneles del rail).
- **`revealUpTo()` / `revealSeq()` / `stagger()`** — `revealUpTo` fija un piso de golpe; `revealSeq(attr, desde, hasta, gap)` fija el piso y hace llegar los niveles nuevos uno detrás de otro; `stagger` revela una lista de niveles. Los tres pasan por `later()`, así que `goto()` los adelanta y el salto sigue reconstruyendo el estado exacto.
- **`speak(el, texto, span, maxStep)`** — el cuarto argumento es la cadencia. Los subtítulos van a 90 ms por palabra; la transcripción de voz a 260 ms, que es velocidad de habla. Las palabras se separan con espacios reales, no con `&nbsp;`, para que un subtítulo largo pueda cortar línea.
- **`fitDevice()` / `syncLog()`** — el teléfono escala desde su borde superior y se centra a mano, porque su caja sin escalar desborda el contenedor. Un `ResizeObserver` sobre `#deviceWrap` y `document.fonts.ready` reajustan las dos cosas cuando el layout se acomoda tarde.
- **El rail** es la pista de argumentación, no decoración: el pipeline de seis nodos, la traza con cuatro canales (Contexto gris, IA cian, Toque ámbar, Sistema verde) y un panel intercambiable (`railPanel('truth'|'filters'|'bound'|'stock'|'biz'|'next')`).
- **Las tarjetas a pantalla completa** (`#zero`, `#inv`, `#invdet`, `#loop`) se superponen a la
  vista dentro del dispositivo y comparten la clase `.zero`. `#zero` es el plan del día al final
  de M1, `#inv` el inventario zona por zona, `#invdet` el contenido de cada zona producto por
  producto, y `#loop` la pantalla de dinero con la que cierra la demo.
- **`speak()` envuelve las palabras dentro del marcado**, no partiendo la cadena. Antes, un `<b>`
  de varias palabras se abría en la primera y quedaba colgando en el resto, así que solo la
  primera salía resaltada. Los subtítulos con énfasis de dos o más palabras estaban mal desde el
  principio, en las dos demos.
- **El panel "Lo que sigue"** (`#next`) entra en el último beat con la escalera de integraciones.
  Es la respuesta a "¿y con qué se conecta esto?", que es la pregunta que sigue al cierre.
- **El cierre.** La demo termina sobre la pantalla del dispositivo, con el resumen del ciclo (`#loop`) encima de la vista de M6. No hay cartel final: se quitó el 4 de septiembre de 2026, en las dos demos, para que la última imagen sea el producto y no una diapositiva. El fin de la reproducción se lleva en la bandera `finished`, que `stop()` levanta y `runBeat()` baja; el botón de reproducir la lee para reiniciar.
- **Regla que atraviesa todo el diseño:** la IA interpreta y propone; el sistema determinista decide la verdad. Fechas, cantidades, alergias y dinero nunca son una inferencia. Si se agrega un momento, tiene que respetarla.

## Verificación

Hay un navegador headless disponible en la máquina:

```
/home/sergio/.cache/ms-playwright/chromium-1234/chrome-linux64/chrome
```

El arnés recorre los 39 beats en móvil y tablet y reporta cinco cosas: vista recortada,
rail desbordado, scroll horizontal, subtítulo metiéndose debajo de los botones de transporte,
y teléfono cortado por su contenedor.

```bash
python3 tools/probe.py                            # los cinco tamaños de ensayo
python3 tools/probe.py 1600x950                   # uno solo
python3 tools/probe.py -f restaurantes.html       # la demo B2B
```

Las dos demos pasan los cinco tamaños con cero desbordes.

Captura de un beat:

```bash
CHROME=/home/sergio/.cache/ms-playwright/chromium-1234/chrome-linux64/chrome
"$CHROME" --headless --disable-gpu --no-sandbox --hide-scrollbars \
  --window-size=1600,950 --virtual-time-budget=25000 \
  --screenshot=/tmp/f20.png "file://$PWD/index.html#b20"
```

Estado al cerrar el Checkpoint 6: **0 desbordes** en 1920×1080, 1600×950, 1440×900, 1366×768 y
1280×720, en móvil y tablet, los 39 beats. Sin errores de consola.

Tres cosas que conviene saber del arnés:

- `tools/probe.html`, el arnés viejo, cargaba la demo en un iframe. Bajo `file://` Chrome trata
  cada archivo como un origen distinto, así que leer `contentWindow.Demo` lanza `SecurityError`
  y el arnés devolvía una página en blanco sin decir por qué. `tools/probe.py` lo reemplaza:
  escribe una copia desechable de `index.html` con el script de medición pegado al final, así
  todo corre en un solo documento. `probe.html` queda solo como referencia.
- `requestAnimationFrame` no avanza bajo `--virtual-time-budget`. Usar `setTimeout`.
- Headless y sin internet las fuentes web nunca cargan, así que las medidas salen con métricas
  de la fuente de reemplazo. Son una buena aproximación, no la proyección exacta.

## Qué se hizo en el Checkpoint 11

Una pantalla nueva en cada demo, pedida por el dueño: hasta ahora M3 solo mostraba los
ingredientes, y faltaba **la receta completa**.

- **Tarjeta `#recipe`** (`.zero.loopstats.recipecard`), justo antes de `#inv` dentro del
  dispositivo. Cabecera con el nombre del plato y sus etiquetas, un bloque de ingredientes que
  reutiliza `.itrow` del detalle de inventario, un bloque de preparación con `<ol class="rc-steps">`
  —número, paso y tiempo— y un pie con la nota de descuento y el botón de cocinar.
- **En la demo B2B** la misma tarjeta es la **ficha técnica**: escandallo por porción con el lote,
  elaboración con tiempos y una fila de puntos críticos (`.rc-ccp`) con temperaturas y alérgenos
  declarados. Es lo que un chef espera ver y lo que ninguna app de hogar tiene.
- **Beat nuevo `m3-recipe`** (6,6 s), entre `m3-unlock` y `m4-cook`. Son **39 beats** y las dos
  demos pasan a durar **192.200 ms**, o sea 3:12.
- **El botón de cocinar se movió a la receta.** `m4-cook` ahora toca `#btnCookR`, el botón que vive
  dentro de la tarjeta, no el `#btnCook` de la vista M3, que queda debajo y sigue existiendo.
  `m4-deltas` quita la tarjeta al entrar a M4.
- **Las cantidades vuelven a ser las mismas en las tres vistas.** 500 g de pollo, 200 ml de crema
  de coco, 1 cebolla y 300 g de arroz en el hogar; 180 g de merluza del lote L-2291, 15 g de
  almidón, 60 ml de crema, 20 g de mantequilla y 40 g de espinaca en B2B. Si se toca una cifra aquí,
  hay que tocarla en `#invdet` y en M4.
- **La tarjeta va centrada** (`justify-content:center`). Se probó arriba y dejaba un tercio de
  pantalla vacío debajo.

Y el sitio publicado, en el mismo checkpoint:

- **Selector de demo** (`.demosel`) en la esquina superior derecha, donde antes estaba la etiqueta
  `CHECKPOINT 6` / `VERSIÓN B2B`, que además ya estaba desactualizada. Son dos enlaces entre
  archivos hermanos, así que no hay estado que sincronizar.
- **La barra superior se apretaba a 1280.** Con el selector adentro se partía en dos filas, le
  robaba 43 px al escenario y el rail desbordaba 25 px en tablet. Se agregó un `@media
  (max-width:1360px)` que esconde el subtítulo de la marca y encoge momentos y botones. La barra
  vuelve a caber en una fila y el desborde desaparece.

Verificación: las dos demos pasan los cinco tamaños en móvil y tablet, 39 beats, con **0
desbordes**.

## Qué se hizo en el Checkpoint 10

Una pantalla nueva en cada demo, pedida por el dueño: después del inventario por zonas, el
**detalle del contenido de cada espacio**, producto por producto y con su cantidad.

- **Tarjeta `#invdet`** (`.zero.loopstats.invdetail`), inmediatamente después de `#inv` dentro del
  dispositivo. Tres bloques `.zone`, uno por espacio de almacenamiento, cada uno con su cabecera
  (icono, nombre, conteo), sus filas `.itrow` — nombre a la izquierda, cantidad en mono a la
  derecha — y un pie `.zone-f` con los productos que no caben en pantalla.
- **Beat nuevo `m1-invdet`** (5,6 s), entre `m1-inv` y `m1-zero`. Son **38 beats** y la demo pasa a
  durar **185.600 ms**, o sea 3:06. Es el primer checkpoint que rompe los 180.000 ms exactos: no
  se recortó pacing de otros beats para conservarlos, porque los que quedan ya están ajustados.
  Si alguna vez hace falta volver a los 3:00 clavados, el ajuste sale de aquí.
- **Las cantidades son coherentes con el resto de la demo**, y esto importa más que el diseño de la
  pantalla: los 500 g de pollo, los 200 ml de crema de coco, el kilo de arroz y las 2 cebollas del
  hogar son exactamente los que M4 descuenta después; en B2B, el lote L-2291 con 6,4 kg de merluza,
  los 4 L de crema y los 4 kg de almidón de maíz son los mismos de M1 y M4. Si se toca una cifra,
  hay que tocarla en las tres vistas.
- **Etiquetas reutilizadas**: `.tag.hot` para lo que vence, `.tag.soon` para lo abierto y para lo
  que está bajo el mínimo o bajo el par.
- **En tablet la tarjeta no pasa a tres columnas.** Se probó y las columnas quedan en unos 170 px:
  los nombres largos y las etiquetas se parten en tres renglones. Se queda en una columna con tipo
  más grande, que en 610×812 sobra espacio.

Verificación: las dos demos pasan los cinco tamaños en móvil y tablet, 38 beats, con **0
desbordes**.

## Qué se hizo en el Checkpoint 9

Tres cambios pedidos por el dueño de la demo, y todos apuntan al mismo lado: **el producto no
habla de sí mismo, y el dinero se muestra, no se enuncia.**

### 1. La interfaz deja de presumir

Se sacó de las dos demos toda la copia que contaba lo que el usuario *no* tiene que hacer:
"ninguno contado a mano", "0 formularios · 0 preguntas · 0 toques", "0 planillas · 0 conteos",
"nadie registra una compra", "nadie escribe una cantidad", "sin conteo", "sin planilla". El
argumento no desapareció: pasó a demostrarse con la experiencia, que era el punto.

Regla nueva, y hay que sostenerla: **la interfaz del producto no dice lo fácil que es usarla.**
La narración de abajo puede argumentar; la pantalla del dispositivo, no.

Las dos tarjetas que eran puro marcador se reemplazaron por contenido:

- **`#zero`** (cierre de M1) pasó de contar formularios a mostrar **el plan**: qué mover hoy,
  qué cocinar o producir primero, y qué falta comprar. En restaurantes, con el dinero en riesgo.
- **El cierre de M4** dejó de ser un "0" gigante y muestra el dinero que se salvó: `$8.40` de
  pollo cocinado a tiempo en el hogar, `$89.60` del lote servido completo en restaurantes.

### 2. El cierre es una pantalla de dinero, con barras

`#loop` ("Una noche / Un servicio, de punta a punta") se eliminó entero y en su lugar va `#pnl`,
una pantalla gráfica del día. Ya no se habla de "menos merma", que no dice nada: se habla de
**lo que se ahorró por aprovechar todo**.

- **Restaurantes**: recaudado del día `$4,182.50`, insumos consumidos `$1,225.50` (29,3% de la
  venta), desperdiciado `$41.90` (1,0%), y debajo margen sobre insumos, ahorro del día y costo de
  alimentos contra el mes anterior. Las tres barras están a escala real de la venta.
- **Hogar**: no hay ingresos, así que la comparación es contra el gasto evitado — cocinado en
  casa `$11.55` contra `$42.00` de pedir lo mismo a domicilio, `$30.45` ahorrados esta noche,
  y el acumulado del mes debajo.

Las barras crecen al entrar (`#pnl.is-live`, igual que `#money` en M6) y `resetScene()` lo baja.

### 3. Las existencias se editan; lo que registra la persona es la verdad

La tarjeta de confirmación de M4 se cayó. En su lugar va `#onhand`: **las cantidades que hay
ahora, con la acción de actualizarlas**. El producto ya no calcula y pide que le confirmen; el
inventario es el dato de la persona y el sistema lo mantiene entre actualizaciones.

La regla, dicha una sola vez y en la propia tarjeta: *"la cantidad que registras es la buena"*, y
en restaurantes queda firmada con hora. El beat `m4-ask` se llama ahora `m4-stock` y la cuarta
fila del panel del rail pasó de **Pregunta** a **Corrige**.

### Tres defectos que salieron al medir

- **`.pbar.rev` chocaba con `.rev`.** La clase de revelación pone `opacity:0`, así que la barra de
  "Recaudado en el día" nunca se veía. Se renombró a `.pbar.sale`. Cuidado al nombrar
  modificadores: `rev`, `ok`, `no`, `sub`, `top` y `is-in` ya están tomados.
- **`.stk` y `.stkline` se confundían a simple vista** siendo cosas distintas. La tarjeta de
  existencias se llama `.onhand`.
- **M4 en móvil de restaurantes ya no daba.** Cuatro descuentos, tres líneas de merma, el aviso de
  par, las existencias y el cierre no caben en un teléfono. Se oculta el aviso de par
  (`.stkline`) solo en móvil: sigue en el rail y en la orden de M5. Mismo criterio que el tercer
  canal de compra de M5.

Verificación: 37 beats, 180.000 ms exactos, cinco tamaños, móvil y tablet, **0 desbordes** y sin
errores de consola en las dos demos.

## Qué se hizo en el Checkpoint 8

El input del usuario deja de estar escondido y pasa a estar **acotado y defendido**. Es la
respuesta a la objeción que la demo se buscaba sola: si el producto promete cero input, la
primera pregunta de la sala la deja sin piso.

El reencuadre tiene dos partes, y las dos ya estaban implícitas en el diseño:

- **Toque ≠ captura.** El rail siempre tuvo un canal ámbar "Toque". Ahora se cuenta y se cobra:
  el cierre dice `4 toques · ningún campo escrito` (hogar) y `5 toques en el turno, todos
  firmados · 0 planillas` (restaurantes). Los números son contables en pantalla, a propósito.
- **Corregir ≠ mantener.** Mantener es continuo y obligatorio — eso es lo que mata a las apps de
  despensa. Corregir es puntual y opcional. El inventario no necesita estar exacto: necesita
  estar suficientemente exacto para la próxima decisión.

Cambios concretos:

- **Beat nuevo `m4-ask`** (5,2 s), entre `m4-list` y `m4-close`. Son **37 beats** ahora, y siguen
  durando **exactamente 180.000 ms**: los 5,2 s salieron de ocho beats con silencio largo
  (`m2-blocked`, `m3-unlock`, `m4-deltas`, `m5-list`, `m5-channel`, `m5-sent`, `m6-money`,
  `m6-loop`), ninguno de los cuales perdió una revelación.
- **Tarjeta `.ask`** en la columna derecha de M4, con las cuatro reglas del input a la vista:
  nunca en blanco (la app afirma su cálculo y pide confirmar), nunca bloquea ("Después", y la
  nota que dice que nada se bloquea), solo si cambia una decisión hoy, y se paga en el acto
  ("no vuelvo a preguntar por el arroz en 3 semanas").
- **Cuarta fila en el panel `#stock` del rail: "Pregunta"**, después de Entra / Sale / Repone.
  Deja ver que preguntar es el último recurso, no el primero.
- **Línea nueva en la traza** (`data-l="24"`, canal Toque). Obligó a correr la numeración de la
  traza: las líneas 24 a 39 pasaron a 25 a 40, en el HTML y en las llamadas `stagger('data-l',…)`
  de M4 a M6. Si se agrega otra línea en el medio, hay que repetir el corrimiento en los dos
  lugares.
- **El cierre `#loop` cuenta toques en vez de negarlos.** La tarjeta `#zero` de M1 conserva
  `0 formularios · 0 preguntas · 0 toques` porque en ese momento sigue siendo literalmente cierto.

En la B2B el input no se esconde: **se vende.** El restaurante ya captura hoy, en planilla y a
mano, porque HACCP se lo exige. La confirmación de M4 queda firmada con nombre y hora, y la nota
lo dice: *"Hoy va en planilla, a mano. Aquí es un toque, y no bloquea el cierre."*

Dos cosas que aparecieron al medir:

- **La compactación de M4 no podía ir en `@media (max-height:760px)`.** La caja del dispositivo
  es de tamaño fijo y se escala, así que el desborde interno es el mismo a 1920×1080 que a
  1280×720. Puesto en la media query, arreglaba las pantallas bajas y rompía las altas. Ahora las
  reglas de M4 son incondicionales y solo el panel del rail —que sí depende del alto de la
  ventana— sigue en media query.
- **El número tiene que ser contable.** El cierre B2B decía "9 movimientos firmados" y en pantalla
  solo se pueden contar 5 toques. Se corrigió a 5. Regla nueva: si el cierre afirma un número,
  tiene que poder contarse viendo la demo.

Verificación: las dos demos pasan los cinco tamaños en móvil y tablet, 37 beats, con **0
desbordes** y sin errores de consola.

## Qué se hizo en el Checkpoint 7

Un solo cambio de enfoque, aplicado a las dos demos: la app deja de *mostrar* el inventario y
pasa a **sugerir qué hacer** con él y a **gestionarlo sola**. Sin beats nuevos: siguen siendo 36
y siguen durando lo mismo. Todo el cambio es contenido, texto y un panel de rail.

- **La acción sugerida entra en la tarjeta del producto** (`.card-a`). Cada lote o producto que
  apura ya no dice solo cuándo vence: dice qué hacer con él hoy. En M1 de las dos demos.
- **Una opción recomendada, no una lista de opciones** (`.rec.top` + `.rec-pick`). La primera
  receta del hogar y el primer plato del restaurante quedan marcados como lo que hay que hacer
  primero. El resto sigue visible, pero deja de competir.
- **El inventario se presenta como algo que se gestiona, no como algo que se consulta.** La
  tarjeta `#inv` gana una fila de gestión (`.invmanage`): en el hogar, cuántos vencen, cuántos
  están bajo el mínimo de la casa y cuántos están abiertos; en restaurantes, cuántos vencen hoy,
  cuántos están bajo el par y cuántos días de cobertura quedan.
- **El mínimo (hogar) y el par (restaurante) se vuelven la razón de la reposición.** En M4 se ve
  qué quedó por debajo (`.stkline`) y en M5 cada línea de la lista o de la orden dice contra qué
  nivel se está pidiendo, en vez de un vago "queda poco".
- **Panel nuevo del rail: `#stock`, "Cómo se mantiene el inventario solo"**, con tres filas —
  Entra por comprobante o factura, Sale por receta o ficha técnica, Repone por mínimo o par. Se
  muestra durante todo M4 y sigue puesto en M5, que es donde la reposición se convierte en pedido.
  Reemplaza al panel `truth` en ese tramo; `truth` vuelve en M6.
- **Subtítulos y traza reescritos en M1, M4 y M5** para que digan sugerencia y gestión, no
  catálogo. El cierre de M1 pasó de "la app abrió hablando" a "la app abrió sugiriendo".

Un defecto real que apareció al medir: `.stkline` ponía la etiqueta y el dato en el mismo flex,
y el dato tiene `white-space:nowrap`; en la columna angosta del tablet de restaurantes la
etiqueta se partía en una palabra por línea. La etiqueta ahora es un `<span>` con `min-width:0`
y el dato no encoge.

Verificación: las dos demos vuelven a pasar los cinco tamaños en móvil y tablet con **0
desbordes**. En restaurantes, M1 en móvil necesitó recortar aire (no texto) para que la línea de
acción cupiera; ese bloque está al final del `<style>`, comentado.

## Qué se hizo en el Checkpoint 6

Solo pulido. Ningún alcance nuevo.

- **Icono de pollo.** El anterior se leía como una llave. Se rehízo como muslo: masa de carne
  arriba a la derecha, hueso corto y nudo doble abajo a la izquierda. Los otros seis no se tocaron.
- **Transiciones entre vistas.** Ya no son seis fundidos idénticos. Cada momento entra con el
  gesto que le corresponde: M1 despierta desde abajo, M2 y M5 avanzan desde la derecha (comparten
  gesto a propósito, las dos abren con una frase hablada), M3 hace push-in al detalle, M4 cae
  desde arriba, M6 entra desde la izquierda porque el pedido *vuelve*.
- **Ritmo.** Los contenidos que aparecían de golpe ahora llegan escalonados (`revealSeq`), y se
  recortaron los silencios largos de cada beat. La demo pasó de 3:08 a **2:56** sin quitar
  ningún beat: son doce segundos de espera muerta que se fueron.
- **Cadencia de la voz.** La transcripción se escribía en menos de un segundo, que no es velocidad
  de habla. `speak()` ahora acepta un paso máximo: los subtítulos siguen rápidos (90 ms por
  palabra, para poder leer adelantado) y la transcripción va a 260 ms, que sí suena a alguien
  hablando.
- **Tipografía.** El subtítulo, que es lo que la sala lee, subió de 1.02 a 1.1 rem, con guardas
  para pantallas bajas.

Y cuatro defectos reales que aparecieron al medir de cerca:

- **El teléfono se cortaba por abajo**: 11 px a 1600×950 y 101 px a 1280×720, desde siempre.
  La caja sin escalar es más alta que su contenedor, y un ítem de grid que desborda se alinea al
  inicio, no al centro; escalarlo desde su propio centro lo empujaba hacia abajo. Ahora escala
  desde el borde superior y el centrado se calcula en JS. De paso el teléfono quedó más grande.
- **El subtítulo no podía cortar línea.** `speak()` unía las palabras con `&nbsp;`, así que una
  frase larga se metía por debajo de los botones de transporte en vez de bajar a la segunda
  línea. Ahora los separadores son espacios normales, el alto de la caja está reservado para dos
  líneas para que el pie no salte, y la ayuda de teclado se esconde bajo 1400 px de ancho.
- **El scroll de la traza quedaba desfasado** si el layout se acomodaba después (fuentes que
  cargan tarde, pantalla completa, cambio de dispositivo). Se guarda la última línea revelada y
  se recalcula. Además el borde superior de la traza ahora se desvanece, para que una línea a
  medio scrollear no quede cortada por la mitad.
- **Las tarjetas de M1 en tablet** partían "Pechuga de pollo" en tres líneas: la columna mide
  unos 250 px y no cabían icono, título y etiqueta en la misma fila. La etiqueta bajó debajo del
  texto.

## Decisiones de este checkpoint

**Audio: no.** La voz sigue siendo solo visual — onda más subtítulo sincronizado, sin audio ni
reconocimiento real. Se consideró `SpeechSynthesis` del navegador, que no exigiría archivos,
y se descartó: la voz disponible cambia según la máquina, puede no existir, y falla en silencio.
La demo tiene que sobrevivir a una sala con ruido, sin internet y con un equipo prestado. Si más
adelante se quiere audio, el lugar correcto son pistas grabadas por beat, no síntesis en vivo.

**Cronometraje con público real: sigue pendiente.** Se recortaron los silencios evidentes con una
regla explícita — que el último elemento de cada beat aterrice entre el 55% y el 75% de su
duración, dejando el resto para leer. Es una regla defendible, pero no reemplaza ver a alguien
mirarla. Es lo único de la lista del Checkpoint 6 que no se puede cerrar sin una sala.

## Deuda conocida

- El panel "Lo que sigue" nombra marcas reales (Rappi, Uber Eats, Instacart, Kroger) y es la
  única parte de la demo que lo hace. Rompe a propósito la decisión de geografía genérica, porque
  la pregunta por las plataformas sale igual. Lo que dice es consistente con
  `docs/03-integraciones-compra.md`: hoy no hay API del lado del comprador en Rappi ni en Uber
  Eats, así que aparecen en el último peldaño y no en el primero. Si se define el país, ese panel
  se ajusta con él.
- Las cifras de dinero están en USD a escala de precios reales de mercado estadounidense, pero
  siguen siendo estimaciones, no una canasta medida. Cuando se defina el país, se reemplazan con
  precios verificados. Es un bloque de HTML, no un rediseño.
- Regla de presentación del dato: **precios solo en USD** (formato `$1,240.60`) y **ningún
  porcentaje sin su comparación explícita**. Todo porcentaje que quede en pantalla dice contra qué
  se compara (turno anterior, mes anterior, otra sede). Si se agrega una cifra, tiene que cumplirla.
- Los canales de compra son genéricos por la misma razón. Con país definido, ganan nombres reales
  y credibilidad.
- El estado mutado de M3 y M5 se restaura clonando el HTML original. Funciona, pero si algún día
  esos botones necesitan listeners reales, hay que cambiar el enfoque.
- En móvil se oculta el tercer canal de compra ("Copiar la lista") para que M5 no se recorte.
  El tablet muestra los tres.
- Bajo 1400 px de ancho se esconde la ayuda de teclado del pie, para que el subtítulo tenga dos
  líneas y no tres. Las teclas siguen funcionando y están listadas acá y en los dos guiones.
- En tablet, M4 y M6 dejan la mitad inferior de la pantalla vacía. Las dos columnas se alinean
  arriba y el contenido no da para más. No es un recorte, es aire de más; arreglarlo sería
  rediseñar la vista, no pulirla.

---

# La demo B2B · `demo/restaurantes.html`

Misma coreografía, mismo motor, mismos 39 beats y los mismos 3:12. Solo cambian el contenido de
las seis vistas, la traza del rail, los tres paneles intercambiables y los subtítulos. Todo lo que
dice "Cómo está construida" y "Verificación" arriba vale igual para este archivo.

## Para quién es

Grupos de 3 a 20 sedes. Es el hueco que identifica `docs/01-analisis-viabilidad.md`: los sistemas
de merma con cámara (Winnow, Orbisk, Leanpath, Kitro) se venden por cotización a grupos grandes y
dejan fuera al restaurante mediano latinoamericano, que sí es atendible con teléfono, etiquetas y
un sensor de USD 20.

## Decisiones tomadas

| Decisión | Valor | Consecuencia |
|---|---|---|
| Segmento | **Grupo de 3 a 20 sedes** | La demo transcurre en la sede Centro, 1 de 4, y M6 cierra con el consolidado del grupo. |
| Espina dorsal | **"Qué produzco hoy y qué me está costando"** | El dinero aparece al final, en puntos de costo de alimentos, que es como se compra esto. |
| Modelo de ingreso | **Suscripción por sede, sin comisión de proveedor** | Se dice en pantalla en M5. En B2B la comisión huele a conflicto de interés y contamina las cifras de costo. |
| HACCP y temperatura | **Detalle de fondo, no momento propio** | Aparece en tres puntos: bitácora de apertura, temperatura de recepción firmada en M6 y "31/31 días" en el cierre. |
| Qué bloquea el plato de M3 | **Alérgeno declarado en la reserva** | Mantiene la regla del producto: una alergia no se resuelve con una inferencia. Y en un restaurante hay responsabilidad legal detrás. |

## Los seis momentos

1. **M1 · El turno ya sabe** — 6:40 a.m., apertura, cero input. FEFO ordena 312 lotes y saca tres con el dinero en riesgo a la vista, cada uno con la **instrucción del día** debajo (sácalo completo hoy, al menú del día, envase abierto). La columna derecha no inventa recetas: dice en qué platos de la carta ya fijada ponerlos, y marca cuál producir primero. Cierra con el inventario vivo — vencen hoy, bajo el par, días de cobertura —, con **el detalle de cada cámara** (qué lote hay y cuánto queda: 6,4 kg de merluza, 18 kg de pollo, 45 kg de arroz) y con el plan del turno.
2. **M2 · Una frase** — *"¿Qué saco para el almuerzo? Vienen 80 cubiertos y me falta un cocinero."* La IA extrae cuatro variables; el contexto aporta el alérgeno declarado en la reserva y la dotación del turno. El sistema multiplica la ficha técnica por 80 cubiertos: 2 platos de 12 entran, 1 queda bloqueado con el motivo visible. Cierra con los 8 campos del ERP colapsando en la frase.
3. **M3 · IA / Sistema** — La chef abre el plato bloqueado. La IA propone almidón de maíz **y dice qué le hace al costo del plato**. La chef acepta. Solo entonces el sistema levanta el bloqueo, recalcula la ficha y firma con nombre y hora.
4. **M4 · Cierra el ciclo** — `Cerrar producción` descuenta nueve insumos por ficha técnica sobre los cubiertos reales, la merma queda registrada con motivo, hora y responsable, en dinero, y cuatro insumos quedan marcados bajo el par. Después las **existencias de la cámara quedan a la vista y editables**: la cantidad que registra la cocina es la buena, firmada con hora. El rail muestra las tres vías por las que el inventario se mantiene solo: entra por factura, sale por ficha técnica, repone por par. Es la respuesta al problema que mata a todo inventario de cocina: mantenerlo cuesta más que el problema que resuelve.
5. **M5 · Al proveedor** — *"Pide lo que falta para mañana."* La orden sale partida en tres, una por proveedor, cada uno con su calendario de entrega, su unidad de compra, su último precio y su mínimo de pedido. Es el momento de negocio, y ahí se declara que no hay comisión de proveedor.
6. **M6 · El costo** — Al día siguiente llega la mercancía. La IA lee la factura, detecta la línea cambiada y el alza, y los cinco lotes entran con cámara, caducidad y temperatura de recepción firmada. Recién ahí aparece el dinero, y cierra con la **pantalla del día en barras**: recaudado `$4,182.50`, insumos consumidos `$1,225.50` (29,3%), desperdiciado `$41.90` (1,0%).

## Qué cambió respecto de la demo de hogar

- **Dispositivo por defecto: tablet.** Es la que hay montada en una cocina. El móvil sigue disponible con `M`.
- **Las recetas dejan de ser el motor.** La carta ya está fijada; el producto solo dice qué plato consume qué lote. Es literal lo que dice el análisis: para un restaurante, las recetas son irrelevantes.
- **Todo movimiento se firma.** Responsable y hora en la sustitución de M3, en la merma de M4 y en la recepción de M6. Es lo que convierte esto en algo auditable ante una inspección.
- **La lista de compras pasa a ser una orden de compra**, agrupada por proveedor y no por pasillo.
- **El ahorro se expresa en puntos de costo de alimentos**, no en pesos ahorrados.
- **Un icono nuevo** (`#i-pescado`) y un bloque de CSS propio al final del `<style>`, comentado, con los ajustes de M6 en móvil y del panel de 8 campos en pantallas bajas.
- **El par, no el ojo del chef, dispara la reposición.** Desde el Checkpoint 7, cada línea de la
  orden de M5 dice contra qué par se está pidiendo y cuánto queda, y M4 marca los insumos que
  cayeron por debajo con su cobertura en servicios. Es el equivalente B2B del mínimo de la casa.

## Deuda conocida propia

- Las cifras siguen siendo placeholder con `$` sin denominar, igual que en la demo de hogar. Los porcentajes de costo de alimentos (31,4% → 29,3%) son plausibles pero no salen de un cliente real.
- Los proveedores son genéricos. Con país definido ganan nombres reales, igual que los canales de compra en la otra demo.
- La integración con ERP se enuncia como un botón ("Exportar al ERP") y no se demuestra. Es la pregunta que más probablemente hagan en la sala.
- El panel "Lo que sigue" de esta demo apunta a Rappi y Uber Eats *por el lado de la oferta*, que
  es el que sí tiene API pública para restaurantes: leer los pedidos de domicilio para pronosticar
  cubiertos y descontar inventario. No es la misma integración que en la demo de hogar, aunque se
  llame igual.
- La confirmación de M4 no cambia nada al tocarla: es una tarjeta estática, como el resto de la
  demo. Si algún día tiene que responder de verdad, hay que darle listeners y sacarla del
  `innerHTML` que restaura `resetScene()`.
- No hay momento de sensor de temperatura en vivo. La bitácora se afirma, no se ve ocurrir. Si se quiere el argumento de inspección en su versión fuerte, ese es el M7 que falta.
- Los pares y la cobertura en días son placeholder, igual que el resto de las cifras. En el
  producto real salen del consumo medido por ficha técnica, que es el dato que la demo ya
  produce en M4; aquí están declarados.
- La bitácora de anoche salió del chip de contexto de M1 para dejar sitio a "3 vencen hoy · 7
  bajo par". Sigue en la traza del rail y en el cierre HACCP de M6, que es donde el argumento de
  inspección pesa de verdad.
