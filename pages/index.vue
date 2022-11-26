<template>
  <div class="home">
    <div class="card-grid">
      <img src="https://bpic.51yuansu.com/pic3/cover/03/59/68/5bd12ce49036d_610.jpg" alt="BLOCKED IN CHINA" width=200px />
      <div style="font-size:50px;">
        <b><br/>因相关法律法规，本页面不予展示</b>
      </div>
    </div>
  </div>
</template>

<script>
import Logo from "~/components/Logo.vue";
import { ReactIcon } from "~/components/Icons.vue";
import SmallCard from "~/components/SmallCard.vue";
import { projects } from "../utils/projectsData";
export default {
  data() {
    return { projects };
  },
  created() {
    // console.log(projects);
  },
  components: {
    Logo,
    ReactIcon,
    SmallCard
  }
};
</script>

<style>
.container {
  margin: 0 auto;
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
}

.title {
  font-family: "Quicksand", "Source Sans Pro", -apple-system, BlinkMacSystemFont,
    "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  display: block;
  font-weight: 300;
  font-size: 100px;
  color: #35495e;
  letter-spacing: 1px;
}

.subtitle {
  font-weight: 300;
  font-size: 42px;
  color: #526488;
  word-spacing: 5px;
  padding-bottom: 15px;
}

.links {
  padding-top: 15px;
}
</style>
