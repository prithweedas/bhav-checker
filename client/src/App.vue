<template>
  <Container />
</template>

<script>
import Container from './components/Container'
export default {
  name: 'App',
  components: {
    Container
  }
}
</script>

<style lang="scss">
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400&display=swap');

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}
html {
  height: 100%;
  font-size: 10px;
}
body {
  font-family: 'Poppins', sans-serif;
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: #ffffff;
}
</style>
