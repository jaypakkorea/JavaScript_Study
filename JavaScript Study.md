# JavaScript Study

_ 2022.10.20



생성자 함수 new

```javascript
function Item(title, price) {
    this.title = title
    this.price = price
    this.showPrice = function() {
        console.log(`가격은 ${price}`)
    }
}

const item1 = new Item('인형', 10000)
const item2 = new Item('가방', 30000)

console.log(item1, item2)
item1.showPrice()
item2.showPrice()
```



```javascript
function makeObj(key, val) {
    return {
        [key] : val
    }
}
const obj = makeObj("나이" , 30)
console.log(obj)
```





```javascript
const user = {
    name : "mike",
    age : 30,
}

const user2 = Object.assign({}, user)    // Object.assign({}, 객체) 를 통한 깊은 복사
const result1 = Object.keys(user)		 // key들만 반환
const result2 = Object.values(user)		 // value들만 반환
const result3 = Object.entries(user)	 // key, value 모두 반환 [ [ 'name', 'Tom' ], [ 'age', 30 ] ]
const result4 = Object.fromEntries(result3)	 // eneries 반대 반환 { name: 'Tom', age: 30 }

user2.name = "Tom"

console.log(user)
console.log(user2)
```



Symbol

```javascript
const user = {
    name : "mike",
    age : 30,
}

const showName = Symbol("show name")

user[showName] = function() {
    console.log(this.name)
}

user[showName]()									// mike

for (let key in user) {
    console.log(`his ${key} is ${user[key]}`)     	// his name is mike
}													// his age is 30

```

