class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {

        HashMap<Character, Integer> char_in_mag = new HashMap<>();
        HashMap<Character, Integer> char_in_ransomNote = new HashMap<>();

        for (char c : magazine.toCharArray()) {
            if (char_in_mag.containsKey(c)) {
                char_in_mag.put(c, char_in_mag.get(c) + 1);
            } else {
                char_in_mag.put(c, 1);
            }
        }

        for (char c : ransomNote.toCharArray()) {
            if (char_in_ransomNote.containsKey(c)) {
                char_in_ransomNote.put(c, char_in_ransomNote.get(c) + 1);
            } else {
                char_in_ransomNote.put(c, 1);
            }
        }

        for (char c : ransomNote.toCharArray()) {
            if (!char_in_mag.containsKey(c) || char_in_mag.get(c) < char_in_ransomNote.get(c)) {
                return false;
            }
        }

        return true;
    }
}
