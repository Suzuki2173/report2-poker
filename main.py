def card_to_string(suit, rank):
    suits = ['S', 'C', 'D', 'H']
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    return suits[suit] + ranks[rank - 1]

def parse_card(card_str):
    suit, rank = map(int, card_str.split())
    return (suit, rank)

def read_cards():
    cards = []
    for _ in range(5):
        card_str = input().strip()
        cards.append(parse_card(card_str))
    return cards

def format_cards(cards):
    return ' '.join([card_to_string(suit, rank) for suit, rank in cards])

def card_ranks(cards):
    return sorted([rank for suit, rank in cards])

def is_flush(cards):
    suits = [suit for suit, rank in cards]
    return len(set(suits)) == 1

def is_straight(ranks):
    return ranks == list(range(ranks[0], ranks[0] + 5))

def classify_by_rank(cards):
    rank_count = {}
    for suit, rank in cards:
        if rank not in rank_count:
            rank_count[rank] = 0
        rank_count[rank] += 1
    return rank_count

def get_hand_rank(cards):
    ranks = card_ranks(cards)
    rank_count = classify_by_rank(cards)
    unique_ranks = len(rank_count)
    rank_freqs = sorted(rank_count.values(), reverse=True)
    
    straight = is_straight(ranks)
    flush = is_flush(cards)
    
    if straight and flush and ranks[-1] == 13:
        return "ロイヤルフラッシュ"
    elif straight and flush:
        return "ストレートフラッシュ"
    elif rank_freqs == [4, 1]:
        return "フォーカード"
    elif rank_freqs == [3, 2]:
        return "フルハウス"
    elif flush:
        return "フラッシュ"
    elif straight:
        return "ストレート"
    elif rank_freqs == [3, 1, 1]:
        return "スリーカード"
    elif rank_freqs == [2, 2, 1]:
        return "ツーペア"
    elif rank_freqs == [2, 1, 1, 1]:
        return "ワンペア"
    else:
        return "ハイカード（ブタ）"

def main():
    cards = read_cards()
    formatted_cards = format_cards(cards)
    hand_rank = get_hand_rank(cards)
    
    print(formatted_cards)
    print(hand_rank)

if __name__ == "__main__":
    main()
