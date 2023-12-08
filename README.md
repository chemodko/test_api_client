# Test API client

This is a framework for testing the API: http://85.192.34.140:8080/swagger-ui/index.html

**Starting auto tests**

```
python -m pytest --reruns 5 --reruns-delay 1 --alluredir=./allure-results

allure serve
or
allure generate
```

