số random sẽ được tạo lại sau mỗi 1 giờ nên có thể tận dụng thông tin trc đó để đoán bằng cnp.


```
random.seed(datetime.strptime(datetime.now().strftime("%Y-%d-%m %H"), "%Y-%d-%m %H").timestamp())
```
