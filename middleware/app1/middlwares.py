def my_middleware(get_response):
    print("Hii my first middleware")

    def my_function(request):
      
      print("This is my secound middleware")
      response = get_response(request)
      print("This is my fourt middlware")
      return response
    return my_function



