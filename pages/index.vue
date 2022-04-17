<template>
  <div class="home">
    <h1>What Can I Deploy to Static Apps?</h1>
    <div class="card-grid">
      <p>
        说点关于后面如何继续建设个人主页的内容。
        <br>
        刚刚在GitHub上搜了不少项目，都是关于Nuxt.js部署静态网站的，主要分为看上去像个人主页的和看上去像个网站的。
        <br>
        <h3>
          <title>看上去像主页的</title>
          <li>
            <ul>https://github.com/claudiabdm/portfolio-2021 <br> 最喜欢的一个之一，可惜并不是开源的</ul>
            <ul>https://github.com/emilsgulbis/portfolio <br> 也是非常有创意的一个主题，同样也不可以直接拿来用，因为没有指定License。但是真的很好看</ul>
            <ul>https://github.com/aynzad/esfahani-nuxt-theme <br> 伊朗的波斯语程序员写的主题，有多语言支持。看起来不错，并且是MIT协议可以白嫖了（笑） </ul>
            <ul>https://github.com/wahyuway/nuxtjs-resume-template</ul>
            <ul>https://github.com/DriesBos/dries-bos-studio</ul>
            <ul>https://github.com/PierreMouchan/portfolio-2019</ul>
            <ul>https://github.com/MarouaneSH/Nuxtjs-vuetify-portfolio</ul>
            <br>
            剩下的几个在设计上各有特色，感觉每一个前端程序员上辈子是不是都是一个出色的UI/UX设计师呢？
          </li>
        </h3>
        <h3>
          <title>看上去像网站的</title>
          <li>
            <ul>https://github.com/mayashavin/tours-nuxt-full-static <br> 来自以色列的一位程序员，nuxtjs大使，做了不少nuxtjs的模板。如果搭团队介绍适合用这个模板</ul>
            <ul>https://github.com/realstoman/nuxtjs-tailwindcss-portfolio <br> 第二选择 </ul>
            <ul>https://github.com/cwray-tech/portfolio-frontend</ul>
            <ul>https://github.com/eggsy/website</ul>
          </li>
        </h3>
        <br>
        <br>
        <big>接下来就请期待鼠宝宝的个人主页的变化喽。顺便之后会加上对使用到的所有开源项目的感谢，以及对送我域名的好朋友的感谢。</big>
      </p>
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
