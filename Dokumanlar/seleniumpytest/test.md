 # Pytest ile Test Otomasyonu Eğitim Dokümanı

## 1. Giriş Konuşması
"Sevgili öğrenciler, bugün Python'da test otomasyonu için kullanılan Pytest framework'ünü öğreneceğiz. Pytest, test yazmayı ve yönetmeyi kolaylaştıran güçlü bir araçtır."

## 2. Pytest Temelleri

### 2.1 Kurulum ve Basit Test
```bash
# Pytest'i kurmak için terminalde aşağıdaki komutu çalıştırın:
pip install pytest
```
```python
# test_basic.py
def test_basic():
    assert 1 + 1 == 2

def test_string_concatenation():
    assert "hello" + " world" == "hello world"

def test_list_concatenation():
    assert [1, 2] + [3, 4] == [1, 2, 3, 4]
```



python
Execute
Copy Code
import pytest

@pytest.fixture
def sample_data():
    return [1, 2, 3, 4, 5]

def test_data_manipulation(sample_data):
    assert len(sample_data) == 5
    assert sum(sample_data) == 15
4.2 Fixture Kapsamları
python
Execute
Copy Code
@pytest.fixture(scope="function")
def function_fixture():
    # Her test fonksiyonu için
    pass

@pytest.fixture(scope="class")
def class_fixture():
    # Her test sınıfı için
    pass

@pytest.fixture(scope="module")
def module_fixture():
    # Her test modülü için
    pass

@pytest.fixture(scope="session")
def session_fixture():
    # Test oturumu boyunca
    pass