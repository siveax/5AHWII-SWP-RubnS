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
        return "Straight Flush"
    if is_flush:
        return "Flush"  # Flash
    if is_straight:
        return "Straight"  # Strasse

    # Wertebasierte Kombis
    return evaluate_rank_combinations(hand)


# --- Simulation und Ausgabe ---

def simulate(games):
    """Spielt X mal und zählt die Ergebnisse."""
    results = {}
    for _ in range(games):
        combo = evaluate_hand(draw_hand())
        results[combo] = results.get(combo, 0) + 1
    return results


def print_results(results, total):
    """Berechnet den prozentualen Anteil und gibt die Ergebnisse aus."""
    print("\n" + "=" * 50)
    print(f"Poker Simulation über {total} Spiele")
    print("=" * 50)

    # Sortierung für übersichtliche Ausgabe (Poker-Hierarchie)
    order = ["Straight Flush", "Four of a Kind", "Full House", "Flush", "Straight",
             "Three of a Kind", "Two Pair", "One Pair", "High Card"]

    sorted_results = {combo: results.get(combo, 0) for combo in order if combo in results}

    for combo, count in sorted_results.items():
        percent = count / total * 100
        print(f"{combo:<18}: {count:<8} ({percent:7.4f} %)")  # Anteil berechnet
    print("-" * 50)


def main():
    # Spiele 100.000 mal und zähle
    GAMES = 100000
    simulation_results = simulate(GAMES)

    # Gib die Ergebnisse aus
    print_results(simulation_results, GAMES)

    # Hinweis zur Aufgabe: Recherchiere die richtigen Anteile und vergleiche
    print("-> Nächster Schritt: Vergleich der Ergebnisse mit theoretischen Wahrscheinlichkeiten.")


if __name__ == "__main__":
    main()