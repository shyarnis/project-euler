extends SceneTree


func _init() -> void:
    var start: float = Time.get_unix_time_from_system()
    var ans: int = solution()
    var finish: float = Time.get_unix_time_from_system()
    var duration: float = finish - start
    print("Answer     = %s" % ans)
    print("Time Taken = %.3f" % duration)
    quit()


func solution() -> int:
    var target: int = 4_000_000
    var sum: int = 0
    var a: int = 0
    var b: int = 1

    while a < target:

        if a % 2 == 0:
            sum += a
        
        # swap(a, b)
        var temp: int = b
        b = a + b
        a = temp
    
    return sum