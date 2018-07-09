context('Index', () => {
    it('Displays all games', () => {
        cy.visit('/')
            .get('[data-cy="game-library"] tr')
            .should('have.length', 4)
            .should('contain', 'Super Mario RPG')
    })
})
