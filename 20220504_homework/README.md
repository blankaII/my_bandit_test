
     ┌────┐                      ┌────┐          ┌────┐                ┌──┐             ┌──────┐                       ┌───────────┐
     │User│                      │WebA│          │WebB│                │DB│             │Bandit│                       │Web_Breeder│
     └─┬──┘                      └─┬──┘          └─┬──┘                └┬─┘             └──┬───┘                       └─────┬─────┘
       │ 30% choose A, 10% choose B│               │                    │                  │                                 │      
       │ ──────────────────────────>               │                    │                  │                                 │      
       │                           │               │                    │                  │                                 │      
       │         10% choose A, 30% choose B        │                    │                  │                                 │      
       │ ──────────────────────────────────────────>                    │                  │                                 │      
       │                           │               │                    │                  │                                 │      
       │                           │         store click history        │                  │                                 │      
       │                           │ ───────────────────────────────────>                  │                                 │      
       │                           │               │                    │                  │                                 │      
       │                           │               │ store click history│                  │                                 │      
       │                           │               │ ───────────────────>                  │                                 │      
       │                           │               │                    │                  │                                 │      
       │                           │               │                    │ AB test algorithm│                                 │      
       │                           │               │                    │ ─────────────────>                                 │      
       │                           │               │                    │                  │                                 │      
       │                           │               │                    │                  │ recommand option base on AB test│      
       │                           │               │                    │                  │ ────────────────────────────────>      
       │                           │               │                    │                  │                                 │      
       │                           │               │      feed greedy option               │                                 │      
       │ <────────────────────────────────────────────────────────────────────────────────────────────────────────────────────      
     ┌─┴──┐                      ┌─┴──┐          ┌─┴──┐                ┌┴─┐             ┌──┴───┐                       ┌─────┴─────┐
     │User│                      │WebA│          │WebB│                │DB│             │Bandit│                       │Web_Breeder│
     └────┘                      └────┘          └────┘                └──┘             └──────┘                       └───────────┘

################################################################################
- http://www.plantuml.com/plantuml/uml/SyfFKj2rKt3CoKnELR1Io4ZDoSa70000

<p><code>
@startuml
User -> WebA : 30% choose A, 10% choose B
User -> WebB : 10% choose A, 30% choose B
WebA -> DB : store click history
WebB -> DB : store click history
DB -> Bandit : AB test algorithm
Bandit -> Web_Breeder : recommand option base on AB test
Web_Breeder -> User : feed greedy option
@enduml
</code></p>
