import warnings
def javascript_alert(msg,pagina_destino=None):
    if pagina_destino == None:
        return f'''
            <script>
                alert("{msg}");
            </script>
            '''
    else:
        return f'''
            <script>
                alert("{msg}");
                window.location.href = "{pagina_destino}";
            </script>
            '''
def deprecated(message):
    def decorator(obj):
        if isinstance(obj, type):
            # Decorador aplicado a una clase
            class DeprecatedClass(obj):
                def __init__(self, *args, **kwargs):
                    warnings.warn(message, category=DeprecationWarning, stacklevel=2)
                    super().__init__(*args, **kwargs)
            return DeprecatedClass
        else:
            # Decorador aplicado a una función
            def new_func(*args, **kwargs):
                warnings.warn(message, category=DeprecationWarning, stacklevel=2)
                return obj(*args, **kwargs)
            return new_func
    return decorator
