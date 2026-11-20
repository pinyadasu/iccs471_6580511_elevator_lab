"""Builder 1 implements the student's policy here."""
from models import Elevator, Request, Decision
import rules

def choose_elevator(elevators: tuple[Elevator, Elevator], request: Request) -> Decision:
    """Choose one eligible elevator according to POLICY.md; never mutate inputs."""
    eligible = rules.eligible_ids(elevators, request)

    if not eligible:
        return Decision(
            None,
            "WAIT: no elevator is eligible because of capacity or route constraints.",
        )

    eligible_elevators = [elevator for elevator in elevators if elevator.id in eligible]

    if len(eligible_elevators) == 1:
        elevator = eligible_elevators[0]
        state = "idle" if elevator.direction == "idle" else f"moving {elevator.direction}"
        distance = abs(elevator.floor - request.floor)
        return Decision(
            elevator.id,
            f"Elevator {elevator.id} is the sole eligible elevator; "
            f"it is {state} and {distance} floor(s) from the request.",
        )

    first, second = eligible_elevators

    first_is_moving = first.direction != "idle"
    second_is_moving = second.direction != "idle"

    if first_is_moving != second_is_moving:
        moving = first if first_is_moving else second
        idle = second if first_is_moving else first
        moving_distance = abs(moving.floor - request.floor)
        idle_distance = abs(idle.floor - request.floor)

        if moving_distance > 4 and idle_distance <= moving_distance - 3:
            return Decision(
                idle.id,
                f"Elevator {idle.id} is idle and {moving_distance - idle_distance} "
                f"floor(s) closer than moving Elevator {moving.id}; "
                "the moving elevator is more than 4 floors away.",
            )

        if moving_distance <= 4:
            return Decision(
                moving.id,
                f"Elevator {moving.id} is already moving and is only "
                f"{moving_distance} floor(s) away, so it is preferred over "
                f"idle Elevator {idle.id}.",
            )

        if idle_distance > moving_distance:
            preference_reason = (
                f"idle Elevator {idle.id} is farther from the request "
                f"({idle_distance} versus {moving_distance} floors)"
            )
        elif idle_distance == moving_distance:
            preference_reason = (
                f"idle Elevator {idle.id} is the same distance "
                f"({moving_distance} floors)"
            )
        else:
            closer_difference = moving_distance - idle_distance
            preference_reason = (
                f"idle Elevator {idle.id} is only {closer_difference} "
                f"floor(s) closer, not the required 3"
            )

        return Decision(
            moving.id,
            f"Elevator {moving.id} is moving and {moving_distance} floors away; "
            f"it is preferred because {preference_reason}.",
        )

    def selection_key(elevator: Elevator) -> tuple[int, int, int]:
        return (
            abs(elevator.floor - request.floor),
            elevator.load_kg,
            0 if elevator.id == "A" else 1,
        )

    chosen = min(eligible_elevators, key=selection_key)
    other = second if chosen is first else first
    chosen_distance = abs(chosen.floor - request.floor)
    other_distance = abs(other.floor - request.floor)

    if chosen_distance < other_distance:
        explanation = (
            f"shorter floor distance: {chosen_distance} versus "
            f"{other_distance} floor(s)"
        )
    elif chosen_distance == other_distance and chosen.load_kg < other.load_kg:
        explanation = (
            f"equal floor distance ({chosen_distance}) and lower load: "
            f"{chosen.load_kg} versus {other.load_kg} kg"
        )
    else:
        explanation = (
            f"equal floor distance ({chosen_distance}) and load "
            f"({chosen.load_kg} kg); deterministic tie-breaker chooses A"
        )

    return Decision(
        chosen.id,
        f"Elevator {chosen.id} is chosen for the same-status tie-break: "
        f"{explanation}.",
    )
