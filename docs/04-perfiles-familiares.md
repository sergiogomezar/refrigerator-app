# FE6 · Perfiles familiares

Feature nueva, propuesta en el refinamiento. Es la forma operativa de FE3: la pantalla donde se ve,
por persona, qué ingredientes puede llevar una receta y cuáles no.

## Ficha de cada miembro

Nombre, color o foto, y **tres listas de ingredientes**:

| Lista | Efecto sobre las sugerencias |
|---|---|
| `no puede` | Excluye la receta por completo |
| `evita` | La baja de orden, pero sigue visible |
| `le encanta` | La sube de orden |

Más un campo de notas libre, que es donde la gente escribe lo que ningún formulario previó.

**Presets** que ahorran armar las listas a mano: vegetariano, vegano, sin cerdo, halal, kosher, sin
lácteos, sin gluten, sin frutos secos, sin mariscos, sin picante. Un toque llena la lista y después
se ajusta.

## Jerarquía de ingredientes

Cada restricción opera por categoría y cubre los derivados:

- "Sin lácteos" debe excluir mantequilla, crema, queso y suero.
- "Sin frutos secos" cubre maní, nueces, almendras y marañón.

Sin esa jerarquía el filtro falla en silencio, que es el peor modo de falla posible: la receta se
muestra como apta y no lo es. Esto implica mantener una taxonomía de ingredientes con categorías
padre, no una lista plana de nombres.

## Resolución por comensales

Antes de sugerir, la app pregunta **quién come**. Con eso:

- Los **prohibidos** son la *unión* de los `no puede` de los presentes. Nunca solo los del que
  cocina.
- Los **penalizados** son la unión de los `evita`.
- Lo que se **destaca** es lo que le gusta a quienes están en la mesa.

**Escenas** guardadas para no repetir la pregunta: `cena familiar`, `solo adultos`, `los niños`,
`solo yo`, e `invitado` — un perfil temporal para la visita que no come algo, que es un caso real y
frecuente.

## Vistas

- **Matriz "quién puede comer qué"**: miembros en las filas, categorías de ingredientes en las
  columnas, y el estado de cada cruce a la vista. Responde de un golpe la pregunta que surge al
  planear la semana, y hace evidente un dato mal ingresado.
- **En cada receta**, para quién sirve y para quién no, con el motivo:
  `sirve para Ana y Luis · no para Sofía (maní)`. Sin el motivo, el usuario no confía en el filtro ni
  sabe cómo corregirlo.

## Comportamientos

- **Sustituir antes de excluir.** Si el choque es un ingrediente reemplazable (leche por bebida
  vegetal, crema por coco), se ofrece la sustitución en vez de borrar la receta del catálogo. Para un
  `evita` se aplica sin más; para un `no puede`, la sustitución se muestra marcada y acompañada del
  aviso de revisar la etiqueta.
- **Transparencia.** La app dice cuánto escondió y por qué (`oculté 4 recetas por maní y cilantro`),
  con opción de verlas. Un catálogo que se vacía sin explicación se siente roto, y el usuario acaba
  borrando sus propias restricciones para que le aparezca algo.
- **Aprende del uso.** Después de "cociné esto", un pulgar por miembro alimenta las listas de `evita`
  y `le encanta`. Las preferencias se construyen usando la app, no llenando un formulario al
  instalarla.

## Reglas que no se negocian

- Un adulto administra los perfiles de menores, y esos perfiles no llevan datos de salud (COPPA en
  Estados Unidos, art. 8 del RGPD, art. 7 de la Ley 1581 en Colombia).
- Sobre lo declarado como `no puede`, la app nunca afirma seguridad: dice "según los ingredientes que
  registramos" y remite a la etiqueta. El filtro es una ayuda, no una garantía.
- Las restricciones se declaran como preferencias de ingredientes, nunca como condiciones médicas.
  Aun así, se tratan internamente como dato sensible: cifrado, sin publicidad segmentada, sin
  compartir con terceros y sin entrenar modelos con ellas, porque una preferencia como "sin gluten"
  puede revelar una condición de salud.

## Por qué vale más de lo que parece

Es lo que hace que la app sirva a una casa y no a una persona. Un inventario compartido sin perfiles
produce sugerencias que a alguien de la mesa no le sirven, y ese es el momento en que la familia deja
de usar la app. Además convierte FE3 en algo concreto y sin riesgo regulatorio: no hay diagnósticos
ni condiciones, solo listas de ingredientes que la propia gente declara.
