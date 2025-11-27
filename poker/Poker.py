import random
import unittest

# ================================
# Poker Simulator
# =================================

# --- Deck modellieren ---
suits = ['♠', '♥', '♦', '♣']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
deck = [rank + suit for suit in suits for rank in ranks]


# --- Funktionen zur Kartenausgabe & Zählung ---

def draw_hand():
    """Gibt zufällig fünf Karten aus."""
    return random.sample(deck, 5)


def count_ranks(hand):
    """Zählt Häufigkeit jedes Kartenwertes für Paare/Drillinge."""
    counts = {}
    for card in hand:
        rank = card[:-1]
        counts[rank] = counts.get(rank, 0) + 1
    return counts


# --- Funktionen für Flush & Straight ---

def check_for_flush(hand):
    """Prüft auf 'Flash' (Flush: gleiche Farbe)."""
    suits_in_hand = [card[-1] for card in hand]
    return len(set(suits_in_hand)) == 1


def check_for_straight(hand):
    """Prüft auf 'Strasse' (Straight: aufeinanderfolgende Werte)."""
    rank_order = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    rank_values = sorted([rank_order.index(card[:-1]) for card in hand])
    is_normal_straight = all(rank_values[i] - rank_values[i - 1] == 1 for i in range(1, 5))
    is_low_ace_straight = set(rank_values) == {0, 1, 2, 3, 12}
    return is_normal_straight or is_low_ace_straight


# --- Funktionen zur Kombinationserkennung ---

def evaluate_rank_combinations(hand):
    """Erkennt alle wertebasierten Kombis (Paar, Drilling, Full House, Poker)."""
    values = list(count_ranks(hand).values())
    if 4 in values:
        return "Four of a Kind"
    elif 3 in values and 2 in values:
        return "Full House"
    elif 3 in values:
        return "Three of a Kind"
    elif values.count(2) == 2:
        return "Two Pair"
    elif 2 in values:
        return "One Pair"
    else:
        return "High Card"


def evaluate_hand(hand):
    """Gibt die höchstmögliche Kombination zurück."""
    is_flush = check_for_flush(hand)
    is_straight = check_for_straight(hand)

    if is_straight and is_flush:
        rank_indices = sorted([ranks.index(card[:-1]) for card in hand])
        if rank_indices == [8, 9, 10, 11, 12]:
            return "Royal Flush"
        return "Straight Flush"

    if is_flush:
        return "Flush"
    if is_straight:
        return "Straight"

    return evaluate_rank_combinations(hand)

# --- UNIT TESTS (2 SUCCESS, 2 FAILURE) ---
class TestPokerLogicSUCCESS(unittest.TestCase):
    """Testet die Kernlogik der Poker-Kombinationserkennung (2 Erfolge, 2 Fehler)."""

    def test_1_full_house(self):
        """SUCCESS: Testet eine korrekte Full House Erkennung."""
        hand = ['K♠', 'K♥', 'K♦', '2♣', '2♠']
        self.assertEqual(evaluate_hand(hand), "Full House", "Sollte Full House erkennen.")

    def test_2_straight_negative_gap_FAILURE(self):
        """FAILURE: Hand ist High Card, aber erwartet wird fälschlicherweise Straight."""
        hand = ['2♠', '3♥', '4♦', '5♣', '7♠']
        self.assertEqual(evaluate_hand(hand), "Straight", "FEHLER SIMULIERT: Ist High Card, erwartet Straight.")

    def test_3_royal_flush(self):
        """SUCCESS: Testet die höchste Kombination (Royal Flush)."""
        hand = ['A♠', 'K♠', 'Q♠', 'J♠', '10♠']
        self.assertEqual(evaluate_hand(hand), "Royal Flush", "Sollte Royal Flush erkennen.")

    def test_4_pure_flush_FAILURE(self):
        """FAILURE: Hand ist Flush, aber erwartet wird fälschlicherweise Straight Flush."""
        hand = ['A♥', 'K♥', 'Q♥', '9♥', '7♥']
        self.assertEqual(evaluate_hand(hand), "Straight Flush", "FEHLER SIMULIERT: Ist Flush, erwartet Straight Flush.")


# --- SIMULATIONS- UND PRINT-FUNKTIONEN ---

def simulate(games):
    """Spielt X mal und zählt die Ergebnisse."""
    results = {}
    for _ in range(games):
        combo = evaluate_hand(draw_hand())
        results[combo] = results.get(combo, 0) + 1
    return results


def print_results(results, total, theoretical_probs):
    """Berechnet den prozentualen Anteil und vergleicht mit theoretischen Werten."""

    print("\n" + "=" * 80)
    print(f"Poker Simulation über {total} Spiele".center(80))
    print("=" * 80)
    print(f"{'Kombination':<20}{'Simuliert (%)':<15}{'Theorie (%)':<15}{'Abweichung (%)':<15}")
    print("-" * 80)

    # Reihenfolge festlegen (Poker-Hierarchie), basierend auf den theoretischen Werten
    order = list(theoretical_probs.keys())
    total_percent_simulated = 0

    for combo in order:
        count = results.get(combo, 0)
        simulated_percent = (count / total * 100) if total > 0 else 0
        total_percent_simulated += simulated_percent
        theoretical_percent = theoretical_probs.get(combo, 0.0)
        deviation = simulated_percent - theoretical_percent

        print(
            f"{combo:<20}"
            f"{simulated_percent:12.4f} %"
            f"{theoretical_percent:12.4f} %"
            f"{deviation:12.4f} %"
        )

    print("-" * 80)
    theoretical_total = sum(theoretical_probs.values())
    print(f"{'Summe (Simuliert/Theorie)':<20}{total_percent_simulated:12.4f} %{theoretical_total:12.4f} %{'':<15}")
    print("=" * 80)


def main():
    # --- Führe die Unit Tests aus (findet TestPokerLogicSUCCESS automatisch) ---
    print("--- Starte Unit Tests ---")

    # Der Test wird ausgeführt und sollte 2 Erfolge und 2 Fehler melden.
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

    print("-------------------------")

    # Theoretische Wahrscheinlichkeiten (Five Card Draw)
    true_percents = {
        "Royal Flush": 0.000154,
        "Straight Flush": 0.001385,
        "Four of a Kind": 0.02401,
        "Full House": 0.1441,
        "Flush": 0.1965,
        "Straight": 0.3925,
        "Three of a Kind": 2.1128,
        "Two Pair": 4.7539,
        "One Pair": 42.2569,
        "High Card": 50.1177
    }

    # Spiele 100.000 mal und zähle
    GAMES = 100000
    simulation_results = simulate(GAMES)

    # Gib die Ergebnisse aus und vergleiche mit true_percents
    print_results(simulation_results, GAMES, true_percents)


if __name__ == "__main__":
    main()