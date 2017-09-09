import java.util.Stack;

/**
 * Created by vgarg on 8/11/17.
 */
public class JoinOrderConvertToDot {
  private static enum tokenType {LEFT_BRACE, RIGHT_BRACE, COMMA, IDENTIFIER, INVALID_TOKEN};

  private static  String currentToken;
  private static int currentPos=0;

  private static tokenType tokenize(final String inputString) {

    // first token should always be '('
    assert (inputString.startsWith("("));
    // last should always be ')'
    assert (inputString.endsWith(")"));

    if(currentPos >= inputString.length()) {
      return tokenType.INVALID_TOKEN;
    }

    switch(inputString.charAt(currentPos)) {
        case '(':
          currentPos++;
          currentToken = "(";
          return tokenType.LEFT_BRACE;

        case ')':
          currentToken = ")";
          currentPos++;
          return tokenType.RIGHT_BRACE;

        case ',':
          currentToken = ",";
          currentPos++;
          return tokenType.COMMA;

          default:
            int saveCurrentPos = currentPos;
            while(inputString.charAt(currentPos) != '(' && currentPos < inputString.length()) {
              currentPos++;
            }
            if(currentPos >= inputString.length()) {
              return tokenType.INVALID_TOKEN;
            }
            while(inputString.charAt(currentPos) != ')' && currentPos < inputString.length()) {
              // bypass the alias
              currentPos++;
            }
            if(currentPos >= inputString.length()) {
              return tokenType.INVALID_TOKEN;
            }
            currentToken = inputString.substring(saveCurrentPos, currentPos+1);
            currentPos++;
            return tokenType.IDENTIFIER;
      }
  }

  private static void printDotFormat(final String inputString) {
    System.out.println("digraph G {");

    tokenType token;
    Stack<String> tokenStack = new Stack<>();
    String joinIdentifier = "JOIN";
    int currentJoinNum = 1;

    do {
      token = tokenize(inputString);
      switch (token){
        case LEFT_BRACE:
          tokenStack.push("");
          break;
        case IDENTIFIER:
          tokenStack.push(currentToken);
          break;
        case RIGHT_BRACE:
          boolean dotLineCreated = false;
          while(tokenStack.peek() != "" && tokenStack.size() > 0){
            String currentIdentifier = tokenStack.pop();
            System.out.println(joinIdentifier + currentJoinNum + " -> " + "\"" + currentIdentifier + "\"");
            dotLineCreated=true;
          }
          tokenStack.pop();
          if(tokenStack.size() != 0 && dotLineCreated) {
            tokenStack.push(joinIdentifier + currentJoinNum);
            currentJoinNum++;
          }
          break;
      }
    }
    while(token != tokenType.INVALID_TOKEN) ;

    System.out.println("}");
  }

  public static void main(String[] args) {
    printDotFormat(args[0]);
  }
}
