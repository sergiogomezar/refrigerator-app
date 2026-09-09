# Freezai

Gestión de inventario de refrigerador para familias, con captura de datos por voz y por foto del
ticket de compra. Este repositorio contiene, por ahora, la documentación de producto: el análisis
de viabilidad de la idea y su refinamiento feature por feature.

## Documentos

| Documento | Contenido |
|---|---|
| [demo/index.html](demo/index.html) | **Demo de visión, hogar.** Coreografía auto-presentada de 3:12 que recorre seis momentos y explica el producto sin que nadie lo narre. Ábrela en el navegador. El traspaso está en [demo/ESTADO.md](demo/ESTADO.md). |
| [demo/restaurantes.html](demo/restaurantes.html) | **Demo de visión, B2B.** La misma coreografía enfocada a grupos de 3 a 20 sedes: FEFO por lote, ficha técnica, merma con motivo y responsable, orden de compra por proveedor y costo de alimentos. |
| [docs/features.html](docs/features.html) · [docs/05-features.md](docs/05-features.md) | **Alcance funcional consolidado.** Las 73 features en 11 áreas, marcadas por fase (v1, v2, futuro). Es el documento para presentar el producto y para planear el desarrollo. |
| [docs/dossier.html](docs/dossier.html) | **Documento consolidado y visual.** Todo el análisis en una sola página: veredicto con indicadores, diagrama del ciclo del inventario, las seis features, resolución de perfiles, mercado, escalera de integraciones, hardware, legislación y hoja de ruta. Ábrelo en el navegador. |
| [docs/00-idea-original.md](docs/00-idea-original.md) | La idea tal como se planteó en la lluvia de ideas, sin refinar. Punto de partida y registro histórico. |
| [docs/01-analisis-viabilidad.md](docs/01-analisis-viabilidad.md) | Viabilidad, tamaño del problema, mercado consumidor frente a restaurantes y hoteles, competencia, hardware, argumentos de venta y límites legales por región. |
| [docs/02-refinamiento-features.md](docs/02-refinamiento-features.md) | Cada feature desgranada en qué se deja, qué se quita y qué se cambia. Alcance de la versión 1 y hoja de ruta. |
| [docs/03-integraciones-compra.md](docs/03-integraciones-compra.md) | Catálogo de plataformas donde se puede cerrar la compra, escalera de opciones y bloqueos que pueden hacer inviable la integración. |
| [docs/04-perfiles-familiares.md](docs/04-perfiles-familiares.md) | Especificación de los perfiles familiares: listas de ingredientes por persona y resolución por comensales. |

Versiones publicadas como página web:

- **Features consolidadas:** https://claude.ai/code/artifact/1e8e097c-b4b2-428e-9275-f47017836d39
- **Dossier de análisis:** https://claude.ai/code/artifact/30b04aff-9640-41e3-98a8-2cd2ca84745b
- Análisis de viabilidad: https://claude.ai/code/artifact/8070d947-89e2-40f0-a7dc-1f8399a00e30
- Refinamiento feature por feature: https://claude.ai/code/artifact/c0adb5a8-8592-44bf-a6cd-e3c41aef5687

## Resumen en diez líneas

1. El problema es real y medible: la EPA calculó en abril de 2025 que una familia de cuatro
   desperdicia cerca de USD 3 000 de comida al año, alrededor del 17% de lo que consume el hogar.
2. Nada de lo planteado es técnicamente difícil en 2026. El riesgo no es técnico, es de retención.
3. La entrada de datos está resuelta con voz y ticket; la salida no. Nadie registra por su cuenta
   lo que se comió. Sin eso, el inventario se desactualiza y las demás features se caen con él.
4. La solución está en la propia lista de features: "cociné esto" con un toque descuenta los
   ingredientes de la receta. Las recetas dejan de ser un adorno y pasan a ser el motor.
5. El hogar es el mercado de crecimiento; los restaurantes y hoteles son el mercado de ingreso.
   Son dos productos distintos y no deben construirse a la vez.
6. El diferencial defendible se acotó en la revisión de mercado del 9 de septiembre de 2026: "en
   español" y "cociné esto" ya los tiene la competencia. Queda la frontera determinista declarada,
   el ticket y el diccionario de productos latinoamericanos, la vida útil con cortes de luz y el
   cierre de la compra en un canal local.
7. La versión 1 no lleva hardware. El sensor Bluetooth de temperatura entra en la versión 2 y no se
   fabrica: se certifican dos modelos comerciales como compatibles.
8. El riesgo legal se concentra en los datos de salud. Con el plan de alimentación tratado como
   preferencia declarada por el usuario, y sin campos clínicos, el panorama se vuelve ordinario.
9. La integración con plataformas de domicilio no se descarta, se ordena en peldaños. Rappi y Uber
   Eats no tienen API de consumidor; Instacart y Kroger sí, y demuestran que el modelo funciona.
10. El siguiente paso no es construir: es una prueba de conserje con diez familias durante dos
    semanas, para responder si la gente registra lo que consume.
