# Field Notes Academy

Field Notes Academy publishes short technical lessons for people who build, test, and operate software. Each lesson starts with a decision, gives you the records a practitioner would see, and asks what those records justify.

## Can you rank two alerting systems?

Two alerting systems run the same 24 checks. You have one slot in a field trial. A check passes when an independent reader confirms that the expected alert arrived before its deadline. A failed read leaves the outcome unknown. These counts are invented for the exercise.

| System | Confirmed passes | Confirmed failures | Unread | Assigned |
| --- | ---: | ---: | ---: | ---: |
| A | 18 | 4 | 2 | 24 |
| B | 17 | 1 | 6 | 24 |

**Make a prediction.** Which system leads on confirmed passes per assigned check? Which leads if you use only checks with a verdict? Write down the two denominators before opening the answer.

<details>
<summary>Compare the results</summary>

Across all assigned checks, A leads with 18/24 (75.0%). B has 17/24 (70.8%). This measure counts confirmed successes against the whole assignment.

Among checks with a verdict, the order reverses. A has 18/22 (81.8%). B has 17/18 (94.4%). Six of B’s outcomes are unread. If the reader times out more often on difficult cases, excluding those cases can change which system looks better.

A could finish with 18–20 passes. B could finish with 17–23. Both an A win and a B win are consistent with the records. Recover the missing outcomes and investigate why B has more unread checks before choosing a system for the trial.

</details>

**Try a changed case.** The reader recovers all six missing B records. Four passed and two failed. Can A still finish ahead on these 24 checks?

<details>
<summary>Check your reasoning</summary>

B finishes with 21 passes. Even if both unread A checks passed, A could reach only 20. That settles the ordering for this sample. A field decision also depends on how well the checks represent real alerts and how much each failure costs.

</details>

## Reproduce the arithmetic

Run `python calculate.py` with Python 3. The script reads the included counts and prints both rates and the possible final pass totals. Edit a copy of the CSV to try another case. No packages, credentials, or network connection are required.

[Input counts](checks.csv) · [Calculation](calculate.py)
