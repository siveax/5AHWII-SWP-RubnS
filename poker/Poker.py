import random

# ================================
# Poker Simulator (Aufgabe Herbstferien)
# =================================

# --- Deck modellieren ---
suits = ['♠', '♥', '♦', '♣']  # Vier Farben
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']  # 13 Symbole

deck = [rank + suit for suit in suits for rank in ranks]  # Erstellt 52 Karten


# --- Funktionen zur Kartenausgabe & Zählung ---

def draw_hand():
    """Gibt zufällig fünf Karten aus."""
    return random.sample(deck, 5)


def count_ranks(hand):
    """Zählt Häufigkeit jedes Kartenwertes für Paare/Drillinge."""
    counts = {}
    for card in hand:
        rank = card[:-1]  # Extrahiere Wert ohne Farbe
        counts[rank] = counts.get(rank, 0) + 1
    return counts


# --- Funktionen für Flush & Straight ---

def check_for_flush(hand):
    """Prüft auf 'Flash' (Flush: gleiche Farbe)."""
    suits_in_hand = [card[-1] for card in hand]
    return len(set(suits_in_hand)) == 1  # Alle Farben identisch?


def check_for_straight(hand):
    """Prüft auf 'Strasse' (Straight: aufeinanderfolgende Werte)."""
    rank_order = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    rank_values = sorted([rank_order.index(card[:-1]) for card in hand])

    # Normale Straße (5-6-7-8-9)
    is_normal_straight = all(rank_values[i] - rank_values[i - 1] == 1 for i in range(1, 5))

    # Spezialfall A-2-3-4-5 (niedrige Straße)
    is_low_ace_straight = set(rank_values) == {0, 1, 2, 3, 12}

    return is_normal_straight or is_low_ace_straight


# --- Funktionen zur Kombinationserkennung ---

def evaluate_rank_combinations(hand):
    """Erkennt alle wertebasierten Kombis (Paar, Drilling, Full House, Poker)."""
    values = list(count_ranks(hand).values())

    if 4 in values:
        return "Four of a Kind"  # Poker (Vierling)
    elif 3 in values and 2 in values:
        return "Full House"
    elif 3 in values:
        return "Three of a Kind"  # Drilling
    elif values.count(2) == 2:
        return "Two Pair"
    elif 2 in values:
        return "One Pair"  # Paar
    else:
        return "High Card"


def evaluate_hand(hand):
    """Gibt die höchstmögliche Kombination zurück."""
    is_flush = check_for_flush(hand)
    is_straight = check_for_straight(hand)

    # Höchste Kombis (Flush & Straight)
    if is_straight and is_flush:
        # Prüfe auf Royal Flush (10, J, Q, K, A in einer Farbe)
        rank_indices = sorted([ranks.index(card[:-1]) for card in hand])

        # Die Indices für 10, J, Q, K, A sind 8, 9, 10, 11, 12
        if rank_indices == [8, 9, 10, 11, 12]:
            return "Royal Flush"

        return "Straight Flush"  # Normale Straße in einer Farbe

    # Reine Flush und Straight
    if is_flush:
        return "Flush"  # Flash
    if is_straight:
        return "Straight"  # Strasse

    # Wertebasierte Kombis
    return evaluate_rank_combinations(hand)


# --- Simulation und erweiterte Ausgabe ---

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

        # Simulierte Berechnung
        simulated_percent = (count / total * 100) if total > 0 else 0
        total_percent_simulated += simulated_percent

        # Theorie
        # Holt den Wert aus dem übergebenen Dictionary
        theoretical_percent = theoretical_probs.get(combo, 0.0)

        # Abweichung berechnen
        deviation = simulated_percent - theoretical_percent

        # Ausgabe
        print(
            f"{combo:<20}"
            f"{simulated_percent:12.4f} %"
            f"{theoretical_percent:12.4f} %"
            f"{deviation:12.4f} %"
        )

    print("-" * 80)
    # Die theoretische Summe ist nicht exakt 100.0000% wegen der Rundung der Einzelwerte
    theoretical_total = sum(theoretical_probs.values())
    print(f"{'Summe (Simuliert/Theorie)':<20}{total_percent_simulated:12.4f} %{theoretical_total:12.4f} %{'':<15}")
    print("=" * 80)


def main():
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