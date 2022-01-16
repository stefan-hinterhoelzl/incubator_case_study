<template lang="html">
  <section class="content">
    <h1>Dashboard - Incubator Digital Twin</h1>
  </section>
  <section>
    <h3>Temperatur: {{temp}}</h3>
    <h3>Fan: {{F}}</h3>
    <h3>Heating: {{H}}</h3>
</section>

</template>
 
<script>
import mqtt from "mqtt";
export default {
  name: "HelloWorld",
  data() {
    return {
      mtopic: "data",
      msg: "no data",
      temp: "N/A",
      H: "N/A",
      F: "N/A",
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
      var json = JSON.parse(message)
      this.temp = (json.temp).toFixed(2);
      this.H = json.H
      this.F = json.F
    });
  },
  methods: {
    handleclick: function() {
      this.client.publish(this.mtopic, this.msg);
    }
  }
};
</script>