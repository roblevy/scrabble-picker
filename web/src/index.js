import React from 'react';
import ReactDOM from 'react-dom';
import axios from 'axios';

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {};
  }

  componentDidMount() {
    axios.get('http://localhost:5000/')
      .then(res => this.setState({
        api_response: res
      }))
  }
  render() {
    return (
      <div>
        <p>This is JSX from React!</p>
        <p>
          {
            this.state.api_response ?
              'Waiting...' :
              this.state.api_response
          }
        </p>
      </div>
    );
  }
}

ReactDOM.render(<App />, document.querySelector('#root'));
