<template lang="html">
  <section class="content">
    <h1>Content Component</h1>
  </section>
  <section>
    <h3>Temperatur: {{temperatur}}</h3>
    <h3>Fan: {{fan_status}}</h3>
    <h3>Heating: {{heating_status}}</h3>
</section>

<div><button class='btn-primary' @click='handleclick()'>Print</button></div>

<div><button class='btn-primary' @click='createConnection'>Connect</button></div>


</template>
 
<script>
import mqtt from "mqtt";
export default {
  name: "HelloWorld",
  data() {
    return {
      mtopic: "/test/topic",
      msg: "lalala",
      client: {}
    };
  },
  mounted() {
    this.client = mqtt.connect("ws://192.168.11.15:9001", { //for stefan
    //this.client = mqtt.connect("ws://ddns.stefanhinterhoelzl.at:9001", { //for thomas
      username: "admin",
      password: "admin"
    });
    this.client.on("connect", e =>{
      console.log("connection succeeded", e);
      this.client.subscribe(this.mtopic, (err)=> {
        if (!err) {
          console.log("Successful subscription:" + this.mtopic);
        }
      });
    });
    this.client.on("message", (topic, message) => {
      this.msg = message
    });
  },
  methods: {
    handleclick: function() {
      this.client.publish(this.mtopic, this.msg);
    }
  }
};
</script>