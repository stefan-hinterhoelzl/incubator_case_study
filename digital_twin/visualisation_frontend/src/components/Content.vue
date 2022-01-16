<template lang="html">
  <section class="content">
    <h1>Dashboard - Incubator Digital Twin</h1>
  </section>
  <section>
    <h2>Aktuelle Daten vom Inkubator</h2>
    <h3>Temperatur: {{temp}}</h3>
    <h3>Fan: {{F}}</h3>
    <h3>Heating: {{H}}</h3>
</section>
<section>
    <h2>Aktuelle Anweisung an den Inkubator</h2>
    <h3>Fan: {{cF}}</h3>
    <h3>Heating: {{cH}}</h3>
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
      cH: "N/A",
      cF: "N/A",
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
      this.client.subscribe("commands", (err) => {
        if(!err) {
          console.log("Successful subscription: commands")
        }
      });

    });
    this.client.on("message", (topic, message) => {
      if (topic == "data") {
        var json = JSON.parse(message)
        this.temp = (json.temp).toFixed(2);
        this.H = json.H
        this.F = json.F
      }
      else if (topic == "commands") {
        var json2 = JSON.parse(message)
        this.cH = json2.H
        this.cF = json2.F
      }
    });
    
  },
  methods: {
    handleclick: function() {
      this.client.publish(this.mtopic, this.msg);
    }
  }
};
</script>