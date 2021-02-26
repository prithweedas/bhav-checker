<template>
  <div class="box">
    <input
      @keyup.enter="$emit('search', searchterm)"
      v-model="searchterm"
      placeholder="Enter name e.g. Reliance"
    />
    <p>*Press enter to search</p>
  </div>
</template>

<script>
export default {
  name: 'SearchBox',
  data() {
    return {
      searchterm: ''
    }
  },
  emits: ['search']
}
</script>

<style lang="scss" scoped>
.box {
  height: 15rem;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  input {
    padding: 1rem 2rem;
    font-size: 3rem;
    font-weight: lighter;
    width: 50rem;
    color: #444;
    border-radius: 5px;
    border: none;
    box-shadow: 0px 3px 15px rgba(0, 0, 0, 0.2);
    &::placeholder {
      font-family: 'Poppins', sans-serif;
      color: #e2e2e2;
    }
    &:focus {
      outline: none;
    }
  }

  p {
    padding: 1rem;
    font-size: 1.2rem;
  }
}
</style>
