/*
* To change this license header, choose License Headers in Project Properties.
* To change this template file, choose Tools | Templates
* and open the template in the editor.
*/
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.Optional;
import java.util.stream.Collectors;

public class solve {
	private Hand blackHand;
	private Hand whiteHand;

	/**
	* Create and run a game when given a hand values.
	*/
	public solve(String hands){
		String[] parts = hands.split("\\s+");

		List<Card> blackCards = new ArrayList<Card>();
		List<Card> whiteCards = new ArrayList<Card>();

		for (int i = 1; i < 6; i++){
			blackCards.add(Card.fromString(parts[i]));
		}
		for (int i = 7; i < 12; i++){
			whiteCards.add(Card.fromString(parts[i]));
		}

		blackHand = new Hand("Black", blackCards);
		whiteHand = new Hand("White", whiteCards);
	}

	public static void main(String args[]) {
		if (args.length == 0){
			System.out.println("No hands provided");
			return;
		}

		String hands = args.length == 1 ? args[0] : String.join(" ", args);
		System.out.println(new solve(hands).getResult());
	}

	public static void mainTest(String[] args){
		String[] inputs = new String[]{
			"Black: 2H 3D 5S 9C KD  White: 2C 3H 4S 8C AH",
			"Black: 2H 4S 4C 2D 4H  White: 2S 8S AS QS 3S",
			"Black: 2H 3D 5S 9C KD  White: 2C 3H 4S 8C KH",
			"Black: 2H 3D 5S 9C KD  White: 2D 3H 5C 9S KH"
		};

		String[] goals = new String[]{
			"White wins. - with high card: Ace",
			"Black wins. - with full house: 4 over 2",
			"Black wins. - with high card: 9",
			"Tie."
		};

		for (int i = 0; i < inputs.length; i++){
			String input = inputs[i];
			solve game = new solve(input);
			String[] hands = game.getHandsString().split("\n");
			String output = game.getResult();
			String goal = goals[i];

			System.out.println("Input : " + input);
			System.out.println("Hands : " + hands[0]);
			System.out.println("      : " + hands[1]);
			System.out.println("Output: " + output);
			System.out.println("Goal  : " + goal + "\n");
		}
	}

	/**
	* Return the hand strings.
	*/
	public String getHandsString(){
		return blackHand + "\n" + whiteHand;
	}

	/**
	* Return the result of the game.
	*/
	public String getResult(){
		Pair<Integer, Optional<Combination>> result = getWinner(blackHand, whiteHand);
		if (result.first != 0){
			Combination combo = result.second.get();
			if (result.first > 0) {
				return "Black wins. - with " + combo + ": " + formatCombination(combo, blackHand);
			} else if (result.first < 0) {
				return "White wins. - with " + combo + ": " + formatCombination(combo, whiteHand);
			}
		}
		return "Tie.";
	}

	public String formatCombination(Combination combo, Hand hand){
		switch(combo.name){
			case HighCard:
				return combo.content.get(0).cardType.toString();
			case FullHouse:
				int pairValue = combo.content.get(0).cardType.value;
				int other = 0;
				for (Card card : hand.cards){
					if (card.cardType.value == pairValue) continue;
					other = card.cardType.value;
					break;
				}

				return (other + 1) + " over " + (pairValue + 1);
			case Pair:
			case TwoPairs:
			case ThreeOfAKind:
			case Straight:
			case Flush:
			case FourOfAKind:
			case StraightFlush:
				return combo.content.stream()
					.map(c -> c.toString())
					.collect(Collectors.joining(", "));
			default:
				return combo.name.toString();
		}
	}

	/**
	* Return the winner.
	*/
	public Pair<Integer, Optional<Combination>> getWinner(Hand first, Hand second){
		Combination firstCombo = first.getMaxCombo();
		Combination secondCombo = second.getMaxCombo();
		int comparision = firstCombo.compareTo(secondCombo);

		Optional<Combination> winningCombo = Optional.empty();
		if (comparision != 0){
			winningCombo = Optional.of(comparision > 0 ? firstCombo : secondCombo);
		}

		return new Pair<Integer, Optional<Combination>>(comparision, winningCombo);
	}

	/**
	 * A generic pair to allow a method to return two differently types objects.
	 */
	public class Pair<T, T2>{
		public T first;
		public T2 second;
		public Pair(T first, T2 second){
			this.first = first;
			this.second = second;
		}
	}

	/**
	* Repersentation of a hand of cards.
	*/
	public class Hand implements Comparable<Hand>{
		private String name;
		private List<Card> cards;

		/**
		* Create hand from cards.
		*
		* @param cards Cards to populate hand with.
		*/
		public Hand(String name, List<Card> cards) {
			this.name = name;
			this.cards = cards;
		}

		@Override
		public boolean equals(Object obj) {
			if (!(obj instanceof Hand)) return false;

			return cards.equals(((Hand) obj).cards);
		}

		@Override
		public String toString(){
			return name + ": " + cards.stream()
				.map(c -> c.toString())
				.collect(Collectors.joining(", "));
		}

		/**
		* Return comparison int against other hand.
		*
		* @param other Hand to compare against.
		*/
		public int compareTo(Hand other){
			if (this.equals(other)) return 0;

			return this.getMaxCombo().compareTo(other.getMaxCombo());
		}

		/**
		* Return the most valuable Combination.
		*
		* @return Most valuable Combination
		*/
		public Combination getMaxCombo() {
			Optional<Combination> straightFlush = getStraightFlush();
			if (straightFlush.isPresent()) {
				return straightFlush.get();
			}

			Optional<Combination> fourOfAKind = getFourOfAKind();
			if (fourOfAKind.isPresent()) {
				return fourOfAKind.get();
			}

			Optional<Combination> fullHouse = getFullHouse();
			if (fullHouse.isPresent()) {
				return fullHouse.get();
			}

			Optional<Combination> flush = getFlush();
			if (flush.isPresent()) {
				return flush.get();
			}

			Optional<Combination> straight = getStraight();
			if (straight.isPresent()) {
				return straight.get();
			}

			Optional<Combination> threeOfAKind = getThreeOfAKind();
			if (threeOfAKind.isPresent()) {
				return threeOfAKind.get();
			}

			Optional<Combination> twoPairs = getTwoPairs();
			if (twoPairs.isPresent()) {
				return twoPairs.get();
			}
			Optional<Combination> pair = getPair();
			if (pair.isPresent()) {
				return pair.get();
			}

			return getHighCards();
		}

		/**
		* All cards have the same value and values are consecutive.
		*/
		private Optional<Combination> getStraightFlush() {
			if (getStraight().isPresent() && getFlush().isPresent()){
				return Optional.of(new Combination(cards, Combination.CombinationName.StraightFlush));
			}
			return Optional.empty();
		}

		/**
		* Four cards have the same value.
		*/
		private Optional<Combination> getFourOfAKind() {
			Optional<List<Card>> threeOfAKind = getOfAKind(4);
			if (!threeOfAKind.isPresent()) return Optional.empty();
			return Optional.of(new Combination(threeOfAKind.get(), Combination.CombinationName.ThreeOfAKind));
		}

		/**
		* Three cards have the same value and the remaining two share the same value.
		*/
		private Optional<Combination> getFullHouse() {
			Optional<List<Card>> threeOfAKind = getOfAKind(3);
			if (!threeOfAKind.isPresent()) return Optional.empty();
			List<Card> threeCards = threeOfAKind.get();
			List<Card> lastTwo = new ArrayList<Card>();
			for (Card card : cards){
				for (Card used : threeCards){
						if (used.cardType.value != card.cardType.value){
							lastTwo.add(card);
							break;
						}
				}
			}

			if (lastTwo.size() != 2 || lastTwo.get(0).cardType.value != lastTwo.get(1).cardType.value){
				return Optional.empty();
			}
			return Optional.of(new Combination(lastTwo, Combination.CombinationName.FullHouse));
		}

		/**
		* All cards have the same suit.
		*/
		private Optional<Combination> getFlush() {
			Suit suit = cards.get(0).suit;
			for (Card card : cards){
				if (card.suit != suit) return Optional.empty();
			}
			return Optional.of(new Combination(cards, Combination.CombinationName.Flush));
		}

		/**
		* Card values are consecutive.
		*/
		private Optional<Combination> getStraight() {
			int[] values = new int[5];
			for (int i = 0; i < cards.size(); i++){
				values[i] = cards.get(i).cardType.value;
			}

			Arrays.sort(values);

			for (int i = 1; i < values.length; i++){
				if (values[i] - 1 != values[i - 1]) return Optional.empty();
			}

			return Optional.of(new Combination(cards, Combination.CombinationName.Straight));
		}

		/**
		* Three cards have the same value.
		*/
		private Optional<Combination> getThreeOfAKind() {
			Optional<List<Card>> threeOfAKind = getOfAKind(3);
			if (!threeOfAKind.isPresent()) return Optional.empty();
			return Optional.of(new Combination(threeOfAKind.get(), Combination.CombinationName.ThreeOfAKind));
		}

		/**
		* There are two pairs of cards that share the same value.
		*/
		private Optional<Combination> getTwoPairs() {
			Optional<Combination> optionalCombination = Optional.empty();
			List<List<Card>> pairs = getAllPairs();
			if (pairs.size() >= 2) {
				List<Card> maxPair1 = getMaxPair(pairs);
				List<Card> content = new ArrayList<>(maxPair1);
				pairs.remove(maxPair1);
				content.addAll(getMaxPair(pairs));
				return Optional.of(new Combination(content, Combination.CombinationName.TwoPairs));
			}
			return optionalCombination;
		}

		/**
		* Two cards have the same value.
		*/
		private Optional<Combination> getPair() {
			Optional<Combination> optionalCombination = Optional.empty();
			List<List<Card>> pairs = getAllPairs();
			if (!pairs.isEmpty()) {
				return Optional.of(new Combination(getMaxPair(pairs), Combination.CombinationName.Pair));
			}
			return optionalCombination;
		}

		/**
		* Highest valued card.
		*/
		private Combination getHighCards() {
			List<Card> sortedCards = new ArrayList<Card>(cards);
			Collections.sort(sortedCards, Collections.reverseOrder());

			return new Combination(sortedCards, Combination.CombinationName.HighCard);
		}

		/**
		* Get all pairs of cards.
		*
		* @return A list of card pairs.
		*/
		private List<List<Card>> getAllPairs() {
			List<List<Card>> pairs = new ArrayList<List<Card>>();

			for (int i = 0; i < cards.size(); i++) {
				Card card1 = cards.get(i);
				for (int j = i + 1; j < cards.size(); j++) {
					Card card2 = cards.get(j);

					if (card1.cardType.equals(card2.cardType)) {
						pairs.add(Arrays.asList(card1, card2));
					}
				}
			}

			return pairs;
		}

		/**
		* Get a number of cards that share the same value.
		*
		* @param number Number of cards to get.
		*/
		private Optional<List<Card>> getOfAKind(int number){
			int[] counts = new int[14];
			for (Card card : cards){
				int value = card.cardType.value;
				counts[value] = counts[value] == 0 ? 1 : counts[value] + 1;
			}

			int value = 0;
			for (int i = 0; i < counts.length; i++){
				if (counts[i] == number){
					value = i;
					break;
				}
			}

			if (value == 0) return Optional.empty();

			List<Card> collection = new ArrayList<Card>();
			for (Card card : cards){
				if (card.cardType.value == value){
					collection.add(card);
				}
			}

			return Optional.of(collection);
		}

		/**
		* Return the most valuable pair of cards.
		*
		* @param pairs Pairs of cards
		*/
		private List<Card> getMaxPair(List<List<Card>> pairs) {
			List<Card> maxPair = pairs.get(0);

			for (List<Card> pair : pairs) {
				if (pair.get(0).cardType.value > maxPair.get(0).cardType.value) {
					maxPair = pair;
				}
			}

			return maxPair;
		}
	}

	/**
	* Represention of a playing card.
	*/
	public static class Card implements Comparable<Card>{
		private Suit suit;
		private CardType cardType;

		/**
		* Create a card with the given suit and type.
		*
		* @param suit Suit of card.
		* @param cardType Type of card.
		*/
		public Card(Suit suit, CardType cardType) {
			this.suit = suit;
			this.cardType = cardType;
		}

		@Override
		public boolean equals(Object object) {
			if (!(object instanceof Card)) return false;

			Card card = (Card) object;
			return this.suit == card.suit && this.cardType == card.cardType;
		}

		@Override
		public String toString(){
			return this.cardType.toChar() + "" + this.suit.toChar();
		}

		/**
		* Return comparison int against other card.
		*
		* @param other Card to compare against.
		*/
		public int compareTo(Card other){
			if (this.cardType.value == other.cardType.value) return 0;

			return this.cardType.value > other.cardType.value ? 1 : -1;
		}

		/**
		* Create a card from a two-character string.
		*/
		public static Card fromString(String string){
			char type = string.charAt(0);
			char suit = string.charAt(1);
			return new Card(Suit.fromChar(suit), CardType.fromChar(type));
		}
	}

	/**
	* A combination of cards.
	*/
	public static class Combination implements Comparable<Combination>{
		private List<Card> content;
		private CombinationName name;

		/**
		* Create a combination of cards.
		*
		* @param content Cards of the combination.
		* @param name Name of the combination.
		*
		*/
		public Combination(List<Card> content, CombinationName name) {
			this.content = content;
			this.name = name;
		}

		/**
		* Return comparison int against other combination.
		*
		* @param other Combination to compare against.
		*/
		public int compareTo(Combination other){
			if (name != other.name) {
				if (name.value > other.name.value) return 1;
				return -1;
			}
			switch (name){
				case HighCard:
					for (int i = 0; i < content.size(); i++){
						Card myCard = content.get(i);
						Card otherCard = other.content.get(i);

						int comparision = myCard.compareTo(otherCard);

						if (comparision == 0) continue;
						if (comparision > 0){
							content = Arrays.asList(myCard);
						}
						else{
							other.content = Arrays.asList(otherCard);
						}
						return comparision;
					}
				default:
					return 0;
			}
		}

		@Override
		public boolean equals(Object object) {
			if (!(object instanceof Combination)) return false;
			return this.content.equals(((Combination) object).content);
		}

		@Override
		public String toString(){
			return name.toString();
		}

		/**
		* All possible combination names.
		*/
		public enum CombinationName {
			HighCard("high card", 1), Pair("pair", 2), TwoPairs("two pairs", 3), ThreeOfAKind("three of a kind", 4), Straight("straight", 5),
			Flush("flush", 6), FullHouse("full house", 7), FourOfAKind("four of a kind", 8), StraightFlush("straight flush", 9);

			private String name;
			private int value;

			private CombinationName(String name, int value) {
				this.name = name;
				this.value = value;
			}

			@Override
			public String toString(){
				return this.name;
			}
		}
	}

	/**
	* All possible suits.
	*/
	public enum Suit {
		clubs('C'), diamonds('D'), hearts('H'), spades('S');

		private char character;

		private Suit(char character){
			this.character = character;
		}

		public char toChar(){
			return this.character;
		}

		/**
		* Return a Suit from a single charater of the starting suit.
		*
		* @param character First character of the desired Suit.
		*/
		public static Suit fromChar(char character){
			for (Suit suit : Suit.values()){
				if (suit.character == character){
					return suit;
				}
			}
			return null;
		}
	}

	/**
	* All possible card types.
	*/
	public enum CardType {
		two('2', 1), three('3', 2), four('4', 3), five('5', 4),
		six('6', 5), seven('7', 6), eight('8', 7), nine('9', 8),
		ten('T', 9), jack('J', 10), queen('Q', 11), king('K', 12), ace('A', 13);

		private char character;
		private int value;

		private CardType(char character, int value) {
			this.character = character;
			this.value = value;
		}

		public char toChar(){
			return this.character;
		}

		/**
		* Return a CardType from a single charater.
		*
		* @param character First character of the desired CardType.
		*/
		public static CardType fromChar(char character){
			for (CardType cardType : CardType.values()){
				if (cardType.character == character){
					return cardType;
				}
			}
			return null;
		}
	}
}
