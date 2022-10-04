#define LED 13
char val;
void setup(){
  pinMode(LED,OUTPUT);
  Serial.begin(9600);
  while (!Serial);
  Serial.println("歡迎來到Arduino");
}

void loop(){
  //Serial.available()會算出目前在buffer內有多少byte的資料
  if(Serial.available()){
    //Serial.read()會讀取第一個byte內的資料,讀取完畢後,buffer內的資料就被刪除。
    //傳送來的資料是char
    val = Serial.read();    
    if(val == '1'){
      digitalWrite(LED,HIGH);
      Serial.println("LED ON");
    }else if(val='0'){
      digitalWrite(LED,LOW);
      Serial.println("LED OFF");
    }
  }
}
