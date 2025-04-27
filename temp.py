import collections
from random import shuffle
from collections import defaultdict

# 1. Структура карты и колоды
Card = collections.namedtuple("Card", ["rank", "suit"])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = "spades diamonds clubs hearts".split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def shuffle(self):
        shuffle(self._cards)


# 2. Определение комбинаций (улучшенная версия)
def evaluate_hand(cards):
    rank_order = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "J": 11,
        "Q": 12,
        "K": 13,
        "A": 14,
    }
    ranks = sorted([rank_order[card.rank] for card in cards])
    suits = [card.suit for card in cards]
    rank_counts = collections.Counter(ranks)
    is_flush = len(set(suits)) == 1
    is_straight = (max(ranks) - min(ranks) == 4) and len(set(ranks)) == 5

    # Определение комбинаций
    if is_straight and is_flush:
        return "Стрит-флеш" if max(ranks) != 14 else "Роял-флеш"
    if 4 in rank_counts.values():
        return "Каре"
    if sorted(rank_counts.values()) == [2, 3]:
        return "Фулл хаус"
    if is_flush:
        return "Флеш"
    if is_straight:
        return "Стрит"
    if 3 in rank_counts.values():
        return "Тройка"
    if list(rank_counts.values()).count(2) == 2:
        return "Две пары"
    if 2 in rank_counts.values():
        return "Пара"
    return "Старшая карта"


# 3. Визуализация статистики в консоли
def print_stats(stats, total):
    print("\n📊 Статистика комбинаций:")
    print("=" * 50)

    max_count = max(stats.values()) if stats else 1
    scale = 30 / max_count  # Масштаб для визуализации

    for combo in [
        "Роял-флеш",
        "Стрит-флеш",
        "Каре",
        "Фулл хаус",
        "Флеш",
        "Стрит",
        "Тройка",
        "Две пары",
        "Пара",
        "Старшая карта",
    ]:
        count = stats.get(combo, 0)
        percent = count / total * 100
        bar = "█" * int(count * scale)
        print(f"{combo:<15}: {percent:6.2f}% | {bar} {count:>6} раз")

    print("=" * 50)


# 4. Основная функция симуляции
def simulate_poker(num_simulations=10000, num_players=4):
    deck = FrenchDeck()
    stats = defaultdict(int)

    for i in range(1, num_simulations + 1):
        deck.shuffle()
        hands = [deck[i * 5 : (i + 1) * 5] for i in range(num_players)]

        for hand in hands:
            stats[evaluate_hand(hand)] += 1

        # Вывод прогресса
        if i % 1000 == 0:
            print(f"Проведено {i} раздач...", end="\r")

    print_stats(stats, num_simulations * num_players)


# Запуск
if __name__ == "__main__":
    print("🎮 Симулятор покерных раздач")
    print("Идет симуляция...")
    simulate_poker(num_simulations=50000, num_players=6)
