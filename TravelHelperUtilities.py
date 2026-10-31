"""Provide simple travel-related utility checks."""


class TravelHelper:
    """Provide currency conversion and baggage weight checks."""

    @staticmethod
    def yen_to_taka(yen):
        """Convert Japanese Yen to Bangladeshi Taka."""
        exchange_rate = 0.85
        return yen * exchange_rate

    @staticmethod
    def check_baggage(weight):
        """Check whether baggage is within the 23 kg limit."""
        return weight <= 23


# Take user input
yen = float(input("Enter amount in Japanese Yen: "))
weight = float(input("Enter baggage weight in kg: "))

# Call static methods directly using the class name
taka = TravelHelper.yen_to_taka(yen)
is_allowed = TravelHelper.check_baggage(weight)

print(f"\nEquivalent amount in Taka: ৳{taka:.2f}")

if is_allowed:
    print("Baggage is within the 23 kg limit.")
else:
    print("Baggage exceeds the 23 kg limit.")