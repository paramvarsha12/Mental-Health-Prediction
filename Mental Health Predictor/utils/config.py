
LABEL_COLUMN = "treatment"


SELECTED_COLUMNS = [
    "family_history",
    "remote_work",
    "benefits",
    "mental_health_interview",
    "coworkers",
    "supervisor",
    "care_options",
    "wellness_program"
]


TARGET_LABELS = {
    0: "Not at Risk",
    1: "At Risk"
}
