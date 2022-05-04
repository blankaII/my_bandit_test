

     ┌────┐                     ┌───┐                 ┌──┐             ┌──────┐
     │User│                     │Web│                 │DB│             │Bandit│
     └─┬──┘                     └─┬─┘                 └┬─┘             └──┬───┘
       │           click          │                    │                  │
       │ ─────────────────────────>                    │                  │
       │                          │                    │                  │
       │                          │ store click history│                  │
       │                          │ ───────────────────>                  │
       │                          │                    │                  │
       │                          │                    │ get click history│
       │                          │                    │ ─────────────────>
       │                          │                    │                  │
       │                          │            recommanded page           │
       │                          │ <──────────────────────────────────────
       │                          │                    │                  │
       │ feed the recommanded page│                    │                  │
       │ <─────────────────────────                    │                  │
     ┌─┴──┐                     ┌─┴─┐                 ┌┴─┐             ┌──┴───┐
     │User│                     │Web│                 │DB│             │Bandit│
     └────┘                     └───┘                 └──┘             └──────┘

################################################################################
- http://www.plantuml.com/plantuml/uml/SyfFKj2rKt3CoKnELR1Io4ZDoSa70000

<code>
@startuml
User -> Web : click
Web -> DB : store click history
DB -> Bandit : get click history
Bandit -> Web : recommanded page
Web -> User : feed the recommanded page
@enduml
</code>
