def test_function():
    def inner_function(a):
        print(a)
    inner_function('Я в области видимости функции test_function')
test_function()

#inner_function()