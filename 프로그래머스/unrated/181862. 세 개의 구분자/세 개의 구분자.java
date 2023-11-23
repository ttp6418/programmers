import java.util.*;
class Solution {
    public String[] solution(String myStr) {
        ArrayList<String> answer = new ArrayList<String>();
        
        String temp = "";
        for(int i=0; i < myStr.length(); i++) {
            if((myStr.charAt(i) == 'a') || (myStr.charAt(i) == 'b' || (myStr.charAt(i) == 'c'))) {
                if(!(temp == "")){ answer.add(temp); temp = ""; }
            }
            else { temp += myStr.charAt(i); }
        }
        if(!(temp == "")){ answer.add(temp); }
        if(answer.size() == 0) { String[] r = new String[1]; r[0] = "EMPTY"; return r; }
        else {
            String[] onlyReturn = new String[answer.size()];
            for (int i=0; i < answer.size(); i++) { onlyReturn[i] = answer.get(i); }
            return onlyReturn;
        }
    }
}