## VariavleByteCode by python  
[reference](https://nlp.stanford.edu/IR-book/html/htmledition/variable-byte-codes-1.html)  
[大規模サービス技術入門](http://gihyo.jp/book/2010/978-4-7741-4307-1)


## Usage
Encode
```
import variable_byte_code as vb
byte_stream = vb.vb_encode(number)
```

Decode
```
import variable_byte_code as vb
number = vb.vb_decode(bytestream)
```
