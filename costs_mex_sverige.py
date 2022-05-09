
def sum_flight_costs_mx_sweden() -> int:
    """
    flight_avg_pesos is a round-trip parting from Mexico City.
    """
    flight_avg_pesos_gdl_to_mx = 3000
    total_gld_mx_round_trip = (flight_avg_pesos_gdl_to_mx * 10) * 2

    flight_avg_pesos_mx_to_sweden = 30_000
    total_mx_sweden_round_trip = flight_avg_pesos_mx_to_sweden * 10
    total_flight_avg_cost = total_gld_mx_round_trip + total_mx_sweden_round_trip

    print(f"Costo vuelo roundtrip Guadalajara-Mexico: ${total_gld_mx_round_trip}")
    print(f"Costo vuelo Mexico-Estocolmo ${total_mx_sweden_round_trip}")
    print(f"Costo promedio en vuelo Guadalajara-Estocolmo ${total_flight_avg_cost}")

    return total_flight_avg_cost


def lodging_costs() -> dict:
    """
    'tax' is an approx.
    """
    airbnb_options = {
        "1": 180_000,
        "2": 310_000,
        "3": 372_000
    }
    for idx, cost in airbnb_options.items():
        extra = cost * .20
        airbnb_options.update({idx: round(cost+extra)})
    return airbnb_options


def total_vacation_trip_to_sweden() -> str:
    print("---TRIP TO STOCKHOLM SWEDEN, PARTING FROM CDMX---")
    lodging_cost = lodging_costs()
    print("Lodging Options:")
    [print(f"\t{k}: ${v}") for k, v in lodging_cost.items()]
    option_input = int(input("Enter an option 1, 2, 3: "))
    trip_cost = sum_flight_costs_mx_sweden()
    total, lodging_sel = 0, 0
    for idx, option in enumerate(lodging_cost, start=1):
        if idx == option_input:
            lodging_sel = lodging_cost.get(option, 0)
            total = lodging_sel + trip_cost
    print(f"Lodging Selection: ${lodging_sel}")
    return f"Total trip in pesos: ${total}"


if __name__ == "__main__":
    print(total_vacation_trip_to_sweden())
