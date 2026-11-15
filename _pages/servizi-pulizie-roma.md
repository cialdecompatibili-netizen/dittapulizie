---
layout: single
title: "Pulizie a Roma"
permalink: /servizi/pulizie-roma/
ref: servizi-roma
description: "Pulizie a Roma: uffici, condomini, case, negozi e fine lavori. Richiedi un preventivo."
seo_description: "Ditta di pulizie a Roma: uffici, condomini, case, negozi, vetrate e pulizie fine lavori. Richiedi un preventivo."
author_profile: false
---

Pulizie a **Roma**: lavoriamo per uffici, condomini, negozi e strutture ricettive di tutta la città. Scegli il servizio che ti serve, oppure mandaci su WhatsApp indirizzo e qualche foto.

{%- assign lista = site.servizi | where: "citta", "Roma" | sort: "title" -%}
{% for s in lista %}
- [{{ s.title }}]({{ s.url | relative_url }}): {{ s.excerpt | strip_html | truncatewords: 22 }}
{% endfor %}

[Tutti i servizi]({{ '/servizi/' | relative_url }})
