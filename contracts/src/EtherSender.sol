// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

contract EtherSender {
    // The constructor is payable so you can optionally deploy
    // with some initial ETH if desired.
    constructor() payable {}

    /**
     * @dev Send 0.01 ETH from this contract to a specified address.
     * Make sure the contract has enough ETH to cover the transfer.
     */
    function sendEther(address payable _to) external {
        require(
            address(this).balance >= 0.01 ether,
            "Not enough balance in contract"
        );

        (bool success, ) = _to.call{value: 0.01 ether}("");
        require(success, "Failed to send Ether");
    }

    /**
     * @dev Return the contract's current balance.
     */
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }

    // Optionally add a fallback function if you want to deposit eth easily:
    fallback() external payable {}
    receive() external payable {}
}
